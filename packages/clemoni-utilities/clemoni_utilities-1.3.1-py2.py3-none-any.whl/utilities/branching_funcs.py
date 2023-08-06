import functools
import sys 


def if_type_test_bool(test, operator, value_test):
    return {
                '>': test > value_test,
                '>=': test >= value_test,
                '==': test == value_test, 
                '<': test < value_test, 
                '<=':test <= value_test, 
                '!=':test != value_test,
    }.get(operator)


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


def if_test_modif_dic(test):
    def reference_dic(origin_dic):
        def keys_value(**keys_value):
            return save_dic(origin_dic)(**keys_value)  if test==True else origin_dic
        return keys_value
    return reference_dic


def if_test_false_log_filter(if_test):
    def reference_dic(collect, test):
        def reference_log(insert_log, *args):
            if if_test==True:
                return (collect, test)
            else:
                return insert_log(*args)
        return reference_log
    return reference_dic


def get_test_dic_value(test_dic):
    return test_dic.values()


def save_dic(dic):
    def wrapper(**update_entry):
        return {**dic, **update_entry}
    return wrapper


def is_valid_test(*,undesired_val=False):
    return lambda test_list_outcome: False if undesired_val in test_list_outcome else True
