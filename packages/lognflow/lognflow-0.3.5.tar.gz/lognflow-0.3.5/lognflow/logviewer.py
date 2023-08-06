import pathlib
import numpy as np
from scipy.io import loadmat
from matplotlib.pyplot import imread

class logviewer:
    def __init__(self,
                 log_dir : pathlib.Path,
                 logger = print):
        self.log_dir = pathlib.Path(log_dir)
        self.logger = logger
        if(self.log_dir.is_dir()):
            self.logger('Looking for a log in: '+ str(self.log_dir))
        else:
            self.logger('No such directory: ' + str(self.log_dir))
        
    def get_text(self, log_name='main_log'):
        flist = list(self.log_dir.glob(f'{log_name}*.txt'))
        flist.sort()
        n_files = len(flist)
        if (n_files>0):
            txt = []
            for fcnt in range(n_files):
                with open(flist[fcnt]) as f_txt:
                    txt.append(f_txt.readlines())
            if(n_files == 1):
                txt = txt[0]
            return txt

    def get_single(self, var_name, single_shot_index = -1, 
                     suffix = '.np*', mat_file_field = None):
        flist = list(self.log_dir.glob(f'{var_name}*{suffix}'))
        if(len(flist) > 0):
            flist.sort()
            var_path = flist[single_shot_index]
            if(not var_path.is_file()):
                return
            self.logger(f'Loading {var_path}')
            if(var_path.suffix == '.npz'):
                buf = np.load(var_path)
                time_array = buf['time_array']
                n_logs = (time_array > 0).sum()
                time_array = time_array[:n_logs]
                data_array = buf['data_array']
                data_array = data_array[:n_logs]
                return(time_array, data_array)
            elif(var_path.suffix == '.npy'):
                return(np.load(var_path))
            elif(var_path.suffix == '.mat'):
                if(mat_file_field is None):
                    mat_file_field = var_path.name
                try:
                    return(loadmat(var_path)[mat_file_field])
                except:
                    self.logger(f'The firld name: {mat_file_field}, '\
                            + f'could not be found in the mat file {var_path}')
        else:
            var_dir = self.log_dir / var_name
            if(var_dir.is_dir()):
                flist = list(var_dir.glob('*.*'))
                flist.sort()
                assert single_shot_index == int(single_shot_index), \
                    f'single_shot_index {single_shot_index} must be an integer'
                var_path = flist[single_shot_index]
                if(var_path.suffix == '.npy'):
                    return np.load(var_path)
                elif(var_path.suffix == '.mat'):
                    if(mat_file_field is None):
                        mat_file_field = var_path.name
                    try:
                        return(loadmat(var_path)[mat_file_field])
                    except:
                        self.logger(f'The firld name: {mat_file_field}, '\
                            + f'could not be found in the mat file {var_path}')
    
    def get_stack_of_files(self, 
        var_name = None, flist = [], 
        return_data = True, return_flist = False):
        
        if not flist:
            assert var_name is not None, \
                ' The file list is empty. Please provide the ' \
                + 'variable name or a non-empty file list.'
            var_dir = self.log_dir / var_name
            if(var_dir.is_dir()):
                var_fname = None
                flist = list(var_dir.glob(f'*.*'))
            else:
                var_fname = var_dir.name
                var_dir = var_dir.parent
                flist = list(var_dir.glob(f'{var_fname}_*.*'))
        if flist:
            flist.sort()
            n_files = len(flist)
            if((not return_data) & return_flist):
                return(flist)
            data_type = None
            if(data_type is None):
                try:
                    fdata = np.load(flist[0])
                    data_type = 'numpy'
                except:
                    pass
            if(data_type is None):
                try:
                    fdata = imread(flist[0])
                    data_type = 'image'
                except:
                    pass
            if(data_type is not None):
                dataset = np.zeros((n_files, ) + fdata.shape, 
                                   dtype=fdata.dtype)
                for fcnt, fpath in enumerate(flist):
                    if(data_type == 'numpy'):
                        dataset[fcnt] = np.load(fpath)
                    elif(data_type == 'image'):
                        dataset[fcnt] = imread(fpath)
                self.logger(f'shape is: {dataset.shape}')
                if(return_flist):
                    return(dataset, flist)
                else:
                    return(dataset)
            else:
                self.logger(f'File {flist[0].name} cannot be opened by '\
                          + r'np.load() or plt.imread()')
            
    def common_files(self, var_name_A, var_name_B):
        
        flist_A = self.get_stack_of_files(
            var_name_A, return_data = False, return_flist = True)
        flist_B = self.get_stack_of_files(
            var_name_B, return_data = False, return_flist = True)
        
        suffix_A = flist_A[0].suffix
        suffix_B = flist_B[0].suffix 
        parent_A = flist_A[0].parent
        parent_B = flist_B[0].parent
        
        fstems_A = [_fst.stem for _fst in flist_A]
        fstems_B = [_fst.stem for _fst in flist_B]
        
        fstems_A_set = set(fstems_A)
        fstems_B_set = set(fstems_B)
        common_stems = list(fstems_A_set.intersection(fstems_B_set))

        flist_A_new = [parent_A / (common_stem + suffix_A) \
                          for common_stem in common_stems]
        flist_B_new = [parent_B / (common_stem + suffix_B) \
                          for common_stem in common_stems]

        return(flist_A_new, flist_B_new)
    
    def replace_time_with_index(self, var_name):
        var_dir = self.log_dir / var_name
        if(var_dir.is_dir()):
            var_fname = None
            flist = list(var_dir.glob(f'*.*'))
        else:
            var_fname = var_dir.name
            var_dir = var_dir.parent
            flist = list(var_dir.glob(f'{var_fname}_*.*'))
        if flist:
            flist.sort()
            fcnt_width = len(str(len(flist)))
            for fcnt, fpath in enumerate(flist):
                self.logger(f'Changing {flist[fcnt].name}')
                fname_new = ''
                if(var_fname is not None):
                    fname_new = var_fname + '_'
                fname_new += f'{fcnt:0{fcnt_width}d}' + flist[fcnt].suffix
                fpath_new = flist[fcnt].parent / fname_new
                self.logger(f'To {fpath_new.name}')
                flist[fcnt].rename(fpath_new)