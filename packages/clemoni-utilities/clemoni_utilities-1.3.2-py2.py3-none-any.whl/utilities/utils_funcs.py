import functools
import sys
from utilities import fp_funcs


def from_iterator_to_list(it):
    return list(it)

def from_string_to_list(string, sep=","):
    return string.split(sep)

def convert_list_val_to_str(a_list):
    return [i if isinstance(i, str) else str(i) for i in a_list]

def from_list_to_string(list_with_str_val, sep=","):
    return sep.join(list_with_str_val)

safe_list_to_string=fp_funcs.compose(from_list_to_string, convert_list_val_to_str)

@fp_funcs.convert_to_map
def add_apostrophe(given_str):
    return f'\"{given_str}\"'

def save_dic(dic):
    def wrapper(**update_entry):
        return {**dic, **update_entry}
    return wrapper


def copy_dic(dic):
    return dic.copy()

def get_empty_dic(*keys):
    return {key:False for key in keys}


def rm_key_from_dic(dic, list_keys, saved_keys=None, saved_dic=None):
    saved_keys = list_keys.copy() if saved_keys is None else saved_keys
    saved_dic = dic.copy() if saved_dic is None else saved_dic

    if len(saved_keys) == 0:
        return saved_dic
    else:
        key = saved_keys.pop()
        del saved_dic[key]
        return rm_key_from_dic(dic, list_keys, saved_keys, saved_dic)


def init_grab_key(dic):
    def grab_key(key):
        return dic.get(key)
    return grab_key

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

