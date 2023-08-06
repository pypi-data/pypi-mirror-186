def if_type_test_bool(test, operator, value_test):
    return {
                '>': test > value_test,
                '>=': test >= value_test,
                '==': test == value_test, 
                '<': test < value_test, 
                '<=':test <= value_test, 
                '!=':test != value_test,
    }.get(operator)

def get_empty_dic(*keys):
        return {key:False for key in keys}
        
def add_message(old_message, new_message):
    return old_message or new_message


def branching(fn, collection_outcome):
    def test_args(*test_args):
        def fn_args(*fn_args):
            def empty_keys(*empty_keys, message):
             
                test_outcome =if_type_test_bool(*test_args) if len(test_args)==3  else test_args 

                return ({**collection_outcome, **fn(*fn_args)} if test_outcome
                else {**collection_outcome, **get_empty_dic(*empty_keys), **{"error_message": add_message(collection_outcome['error_message'], message)}})
            return empty_keys
        return fn_args
    return test_args
