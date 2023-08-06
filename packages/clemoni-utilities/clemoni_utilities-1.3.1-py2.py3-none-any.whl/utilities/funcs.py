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

save_list_to_string=fp_funcs.compose(from_list_to_string, convert_list_val_to_str)


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
def test_size_list(list, expected_size, operator):
    return len(list), expected_size, operator


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