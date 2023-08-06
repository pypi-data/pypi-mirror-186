# General function use in multiple script 
#  like compose to for currying 
#  or function create files, folder and so one 


import os
from os import listdir, path, scandir, remove, rmdir
from os.path import isfile, join
import functools
import sys
import shutil
from pathlib import Path


def apply_fun_to_list(*, func, success_message):
    """Apply a func to all the element of list

    Parameters
    ----------
    func : function
        a function that will be apply to element 
    success_message : str
        a success message is printed in case of success.
    """
    def wrapper(*, given_list, **kwargs):
        try:
            for i in given_list: func(i)
        except Exception as e:
            print(f"""
            Oups... Something went wrong!
            {e}""")
        else:
            print(f"{success_message}")
        
    return wrapper


#  MASKS / TEST FUNCTION

def if_regex_return_value(fn):
    """Function test, use later as a mask 
    form regex function. 
    If regex function return a value, then return the first founded value. 

    Parameters
    ----------
    fn : function
        a regex function

    Returns
    -------
    'str'
        the regex matched value
    """
    @functools.wraps(fn)
    def wrapper(value):
        regex_test = fn(value)
        if regex_test:
            return regex_test.group(0)
        else:
            return None
    return wrapper


def exit_if_error(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        output = fn(*args, **kwargs)
        if output==False:
            sys.exit()
        else:
            return output
    return wrapper


def try_except_all(fn):
    """Run a function 
    inside a TRY except Exception

    Parameters
    ----------
    fn : function
        the function that can genereate errors 
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit()
    return wrapper


def if_test_fn_1_else_fn_2(*, fn_1, fn_2, test):
    """IF ESLE Test. 
    IF test true, function 1 is run 
    else function 2 is run. 

    Same arguments is parsed to both functions.

    Parameters
    ----------
    fn_1 : funcion

    fn_2 : function

    test : a value to be tested

    """
    def wrapper(value_test, **kwargs):
        return fn_1(**kwargs) if test == value_test else fn_2(**kwargs)
    return wrapper


def if_fn_test_fn_1_else_fn_2(*, fn_1, fn_2, fn_test):
    """IF ESLE Test. 
    IF test true, function 1 is run 
    else function 2 is run. 

    Same arguments is parsed to both functions.

    Parameters
    ----------
    fn_1 : funcion

    fn_2 : function

    test : a value to be tested

    """
    def wrapper(**kwargs):
        return fn_1(**kwargs) if fn_test else fn_2(**kwargs)
    return wrapper



def if_type_test_bool(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        test, value_test, operator = fn(*args)
        return {
                '>': test > value_test,
                '>=': test >= value_test,
                '==': test == value_test, 
                '<': test < value_test, 
                '<=':test <= value_test, 
                '!=':test != value_test
        }.get(operator)
    return wrapper

def if_test_is_value_test_return_test_none(fn):
    def wrapper(test, value_test, operator):
        test_result=fn(test, value_test, operator)
        return test if test_result else None
    return wrapper
    
@if_type_test_bool
def test_size_folder(folder_path, expected_size, operator):
    return len(get_file_object_from_dir(folder_path)), expected_size, operator


@if_type_test_bool
def test_size_list(list, expected_size, operator):
    return len(list), expected_size, operator
    
# _________________________________________________
# FUNCTIONAL PROGRAMMING 

def compose(g, f):
    def h(*args):
        return g(f(*args))
    return h

def compose_bis(g, f):
    def h(x):
        return g(f(x))
    return h


def compose_3(h, g, f):
    def i(*args):
        return h(g(f(*args)))
    return i


def compose_4(i, h, g, f):
    def j(*args):
        return i(h(g(f(*args))))
    return j

def compose_5(j, i, h, g, f):
    def k(*args):
        return j(i(h(g(f(*args)))))
    return k


def compose_f_input(g, f):
    def h():
        return g(f())
    return h

# ______________________________________________________
#FILES AND FOLDER 

@exit_if_error
def check_given_folder(path):
    """Check if a path exist

    Parameters
    ----------
    path : str
        the path that wants to be used 

    Returns
    -------
    Path
        the given path

    Raises
    ------
    ValueError
        if not path given or path invalid raise error and sys.exit
    """
    try:

        given_path=Path(path)

        if given_path.exists()==False:
            raise ValueError("Given path does not exist.")
      
    except IndexError:
            print(f'ERROR: No folder path has been given')
            
            
    except Exception as e:
        print(f'ERROR: {e}')
        return False
    
    else:
        return given_path


def get_file_from_dir(dir_path):
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
    return [file.name for file in scandir(dir_path) if file.is_file() and file.name!='.DS_Store']

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

def get_file_from_dir_if_extension(dir_path, extension_test):
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
    
    output= [file.path for file in scandir(dir_path) if file.is_file() and file.name.endswith(extension_test)]
    return output

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

def get_the_latest_insert(fn_get_document):
    def wrapper(*args):
        return max(fn_get_document(*args), key=os.path.getctime)
    return wrapper


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
    os.makedirs(sub_dir, exist_ok=True)
    return sub_dir 

@try_except_all
def redirect_file(origin_path, export_path, renamed_file):
    shutil.copyfile(f"{origin_path}", f"{export_path}/{renamed_file}")

@try_except_all
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
 

@try_except_all
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
# ______________________________________________________
# OTHERS

def flatten_list(nested_lists):
    """
    Flatten nested list in 
    one list
    Parameters
    ----------
    res : [list]
        A nested list
    Returns
    -------
    [list]
        a flatten list
    """
    output = []
    for nested_list in nested_lists:
        output = [*output, *nested_list]
    return output


def confirm_choice():
    try:
        comfirm_prompt = input('Can you confirm your choice [Y/N]? ')
        test_value = comfirm_prompt.lower()
        if not test_value:
            raise ValueError('No answer given')
        if test_value not in ['y', 'n']:
            raise ValueError(
                f"""
                The value you entered ({comfirm_prompt}) is invalid.
                Must be either Y or N.
                """)
    except Exception as e:
        print(e)
        return confirm_choice()
    else:
        print(f'Choice confirmed: {comfirm_prompt}\n')
        return test_value


def yes_no_prompt(question):
    try:
        comfirm_prompt = input(f'{question} [Y/N]? ')
        test_value = comfirm_prompt.lower()
        if not test_value:
            raise ValueError('No answer given')
        if test_value not in ['y', 'n']:
            raise ValueError(
                f"""
                The value you entered ({comfirm_prompt}) is invalid.
                Must be either Y or N.
                """)
    except Exception as e:
        print(e)
        return yes_no_prompt(question)
    else:
        print(f'Choice confirmed: {comfirm_prompt}\n')
        return test_value

# Grab key of a given dictionnary
def init_grab_key(dic):
    def grab_key(key):
        return dic.get(key)
    return grab_key