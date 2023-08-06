
from os import path, scandir, remove, rmdir, getcwd, makedirs
from os.path import isfile, join
import functools
import sys
import shutil
from pathlib import Path
from utilities import branching_funcs


def compose(g, f):
    def h(arg):
        return g(f(arg))
    return h



def handle_exhauted_max(fn_max):
    @functools.wraps(fn_max)
    def wrapper(args):
        try:
            value=fn_max(args)
        except ValueError as e:
            return None
        else:
            return value
    return wrapper


def test_path(path):
    try:
        tested_path=Path(path).exists()
        if tested_path==False:
            raise ValueError(f'{path} given is not a valid path')
    except ValueError as e:
        print(e)
        return None
    else:
        return tested_path

def is_path_exists(path):
    return Path(path).exists()


def get_scandir_iterator(path):
    return scandir(path)


def remove_ds_store(entry):
    return True if entry.name!=".DS_Store" else False


def get_filter(filter_type):

    def is_file(entry):
        return True if entry.is_file() else False

    def is_folder(entry):
        return True if entry.is_dir() else False

    return {
        "file":is_file,
        "folder":is_folder
        }.get(filter_type)


def get_output_type(output):

    def to_list(scandir_iteraror):
        return list(scandir_iteraror)

    
    @handle_exhauted_max
    def to_last_modified(scandir_iteraror):
        """get last modified entry (file/folder)
        from list of files/folders.

        can be a list or scandir ie. get_last_modif_from_dirs_entry(scandir(path))

        Args:
            dirs_entry_list (list/scandir): _description_

        Returns: last modifed element
        """
        return max(scandir_iteraror, key=path.getmtime)  

    
    get_size=compose(lambda x:len(x),lambda x:list(x))

    return {
        'list':to_list,
        'size':get_size,
        'last_modifed':to_last_modified
    }.get(output)


def get_entry_object(path):
    tested_path=test_path(path)

    def wrapper(*,filter_type=None, output=None):

        if tested_path:

            scandir_it=get_scandir_iterator(path)

            filter_output = scandir_it if filter_type is None else filter(get_filter(filter_type),scandir_it)

            no_DS_store_file=filter(remove_ds_store, filter_output)

            return no_DS_store_file  if output is None else get_output_type(output)(no_DS_store_file)

    return wrapper




def get_file_object_from_dir(dir_path):
    """ Retrieves all files from a given directory

    Parameters
    ----------
    dir_path : str
        the path of the directory

    Returns
    -------
    list
        a list of files name
    """
    return [file for file in scandir(dir_path) if file.is_file() and file.name!='.DS_Store']



def get_file_object_from_dir_if_extension(dir_path, extension_test):
    """ Retrieves all files from a given directory

    Parameters
    ----------
    dir_path : str
        the path of the directory

    Returns
    -------
    list
        a list of files name
    """
    
    output= [file for file in scandir(dir_path) if file.is_file() and file.name.endswith(extension_test)]
    return output


def delete_all_files_from_dir(path):
    """Delete all the files from a given directory

    Parameters
    ----------
    dir_path : string
        path of teh directory
    """
    for file in scandir(path): 
        if file.is_file: 
            remove(file.path)
    print(f'All files from {path} are now deleted.')



def delete_all_folders_from_dir(path):
    """Delete all the files from a given directory

    Parameters
    ----------
    dir_path : string
        path of teh directory
    """
    for folder in scandir(path):
        if folder.name !='.DS_Store':
            shutil.rmtree(folder.path)
    print(f'All folder from {path} are now deleted.')



def create_sub_directory(*, path_name, folder_name):
    """Create a subdirection under a given path

    Parameters
    ----------
    path_name : str
        the parent dicterory
    folder_name : str
        the name of the sub_directory

    Returns
    -------
    str
        the path to the newly created subdirectory 
    """
    sub_dir=path.join(path_name, folder_name)
    makedirs(sub_dir, exist_ok=True)
    return sub_dir 

@branching_funcs.try_except_all
def redirect_file(origin_path, export_path, renamed_file):
    shutil.copyfile(f"{origin_path}", f"{export_path}/{renamed_file}")

@branching_funcs.try_except_all
def redirect_file_object(file_object, dist, renamed_file=None):
    """Redirect a file object (fn: get_file_object_from_dir)
    to a given path 

    If no name is given take by default the current name of the file 

    Parameters
    ----------
    file_object : obj
        the file object (name, path)
    dis : str
        the destination path the the file will be directed 
    renamed_file : str, optional
        the new name of the file , by default take the name attribut from file object
    """
    renamed_file= file_object.name if renamed_file is None else renamed_file
    shutil.copyfile(file_object.path, f"{dist}/{renamed_file}")
 

@branching_funcs.try_except_all
def redirect_folder(folder_object, dist, renamed_folder=None):
    """Redirect a folder object (fn: get_folder_object_from_dir)
    to a given destination

    If not name is given the redirected folder will take the current folder
    name by default

    Parameters
    ----------
    folder_object : obj
        the folder object (name, path)
    dist : str
        the destination folder
    renamed_folder : _type_, optional
        _description_, by default None
    """
    renamed_folder= folder_object.name if renamed_folder is None else renamed_folder
    shutil.copytree(folder_object.path, f"{dist}/{renamed_folder}")

def get_folder_from_dir(dir_path):
    """Get all the folder path 
    from fiven path

    Parameters
    ----------
    dir_path : str
        path to locate the folders

    Returns
    -------
    list
        list of all available folders path
    """
    return [folder.path for folder in scandir(dir_path) if folder.is_dir()]

def get_folder_object_from_dir_if_name(dir_path, name_test):
    """Get all folder object from 
    given path if name match certain value

    Parameters
    ----------
    dir_path : str
        path to locate folders
    name_test : str
        the name check if exist
    Returns
    -------
    list
        the list of the folders avaiable at the given path matching a specifi value
    """

    return [folder for folder in scandir(dir_path) if folder.is_dir() and name_test in folder.name]

def get_folder_object_from_dir(dir_path):
    """Get all the folder object 
    from fiven path

    Parameters
    ----------
    dir_path : str
        path to locate the folders

    Returns
    -------
    list
        list of all available folders object

    """
    return [folder for folder in scandir(dir_path) if folder.is_dir()]

def is_subfolders(dir_path):
    return True if len(get_folder_object_from_dir(dir_path))!=0 else False