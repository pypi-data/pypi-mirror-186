"""
Gives the possibility to add a package from another folder
external to the current folder. 
In this project mainly use to load the library package folder.

"""
import sys

from os import  getcwd, path
from pathlib import Path

import re
import functools

# ________________________________________________________________

# General function


def compose(g, f):
    """Chain two functions

    Parameters
    ----------
    f : function
        First function 
    g : function
        Second function
    arg: argument to be given 
    in the second level of the function architecture.
    """
    def h(arg):
        return g(f(arg))
    return h

def compose_3(h, g, f):
    def i(*args):
        return h(g(f(*args)))
    return i



def if_regex_return_true(fn):
    @functools.wraps(fn)
    def wrapper(value):

        return True if fn(value) else False

    return wrapper

@if_regex_return_true
def is_slash_path(path):
    return re.match(r'^/', path)


def remove_first_slash_from_path(path):
    return path.strip('/')

def handle_first_slash_path(path):
    return remove_first_slash_from_path(path) if is_slash_path(path) else path

# ________________________________________________________________

# Add a other package function 
def get_current_file():
    """Return the folder 
    where the current file is located

    Returns
    -------
    string
    The folder where the file is located. 
    """
    return path.dirname(__file__)

def add_package_folder(path_to_package, fn_get_current_file=get_current_file):
    """
    Create a path from the current folder location

    Parameters
    ----------
    fn_get_current_file : function, optional
        the current folder where the file is located, by default get_current_file
    """
    return path.join(fn_get_current_file(), path_to_package)
    

def append_package_to_path(package_path):
    """
    Add new Python path.

    Parameters
    ----------
    package_path : string
        The package name to be added to the new Python path
    """
    sys.path.append(package_path)

def handle_if_path_exist(test_path):
    return path if Path(test_path).exists() else None
 


def get_path_dynamically(folder_name, limit=6, start=None, checked_folder_name=None):
    limit=6 if limit is None else limit
    start=0 if start is None else start
    checked_folder_name=handle_first_slash_path(folder_name) if checked_folder_name is None else checked_folder_name


    if start<=limit:

        tested_path=add_package_folder(checked_folder_name)

        if Path(tested_path).exists():
            return tested_path
        else:
            checked_folder_name=f"../{checked_folder_name}"
            
            start+=1

            return get_path_dynamically(folder_name, limit, start, checked_folder_name)

    else:
        print(f"Error: Could not find path for file {folder_name}")
        return False



append_package_dynamically=compose(append_package_to_path, get_path_dynamically)
