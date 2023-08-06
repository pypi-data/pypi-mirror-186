
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



def secure_answer_from_prompt(input_text, expected_value_list, sensible_to_case=True):

    expected_value_list_str= [str(i.lower()) for i in expected_value_list] if sensible_to_case==False else [str(i) for i in expected_value_list]

    try:
        comfirm_prompt = input(input_text)
        comfirm_prompt = comfirm_prompt.lower() if sensible_to_case==False else comfirm_prompt

        if not comfirm_prompt:
            raise ValueError('No answer given')

        if comfirm_prompt not in expected_value_list_str:
            raise ValueError(
                 f"""
                The value you entered ({comfirm_prompt}) is invalid.
                Must be either {" or ".join(expected_value_list_str)}.
                """)
    except Exception as e:
        print(e)
        return secure_answer_from_prompt(input_text, expected_value_list)
    else:
        print(f'Choice confirmed: {comfirm_prompt}\n')
        return comfirm_prompt