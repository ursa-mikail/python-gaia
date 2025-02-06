####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/text')
sys.path.append(lib_path)

# import package from path
from regex_lib import regex_lib	# file name

def regex_lib_test_00():
    id_regex_lib = "Test Usage Agent: <regex_lib>"
    print ("=====[" + id_regex_lib + " Start]===== \n")
    regex_lib_object = regex_lib(id_regex_lib)

    regex_lib_object.who_am_i()

    target_string = r"   12300hello==456world-URSA-MAJOR-111-789\\000{}+`000"
    print("target_string: ", target_string)
    [matched_substrings, locations] = regex_lib_object.find_alphabets_in_target_string(target_string)
    print(matched_substrings, " at ", locations)
    [matched_substrings, locations] = regex_lib_object.find_alphabets_in_target_string(target_string, 'UPPERCASE')
    print(matched_substrings, " at ", locations)
    [matched_substrings, locations] = regex_lib_object.find_alphabets_in_target_string(target_string, 'LOWERCASE')
    print(matched_substrings, " at ", locations)


    [matched_substrings, locations] = regex_lib_object.find_numbers_in_target_string(target_string)
    print(matched_substrings, " at ", locations)
    [matched_substrings, locations] = regex_lib_object.find_ascii_symbols_in_target_string(target_string)
    print(matched_substrings, " at ", locations)
    N = 5
    [matched_substrings_with_N_alphabets, locations_with_N_alphabets] = regex_lib_object.find_N_alphabets_in_target_string(target_string, N, 'IGNORECASE')
    print(matched_substrings_with_N_alphabets, " at ", locations_with_N_alphabets)
    N = 3
    [matched_substrings_with_N_numbers, locations_with_N_numbers] =  regex_lib_object.find_N_numbers_in_target_string(target_string, N)
    print(matched_substrings_with_N_numbers, " at ", locations_with_N_numbers)
    N = 4
    [matched_substrings_with_N_ascii_symbols, locations_with_N_ascii_symbols] =  regex_lib_object.find_N_ascii_symbols_in_target_string(target_string, N)
    print(matched_substrings_with_N_ascii_symbols, " at ", locations_with_N_ascii_symbols)

    string_filtered = regex_lib_object.remove_numbers_from_target_string(target_string)
    print("string_filtered: ", string_filtered)
    string_filtered = regex_lib_object.remove_ascii_symbols_from_target_string(target_string)
    print("string_filtered: ", string_filtered)
    string_filtered = regex_lib_object.remove_alphabets_from_target_string(target_string)
    print("string_filtered: ", string_filtered)

    [matched_substrings, locations] = regex_lib_object.find_alphabets_in_target_string(string_filtered)
    print(matched_substrings, " at ", locations)

    string_filtered = regex_lib_object.remove_alphabets_from_target_string(target_string, 'UPPERCASE')
    print("string_filtered: ", string_filtered)
    string_filtered = regex_lib_object.remove_alphabets_from_target_string(target_string, 'LOWERCASE')
    print("string_filtered: ", string_filtered)

    # import _Gaia._gaia
    # help(regex_lib) # introspect
    import re

    str = 'ursa-major@==.com'
    str = 'ursa-111@==.com'
    str = 'ursa-111@==.com'
    str = 'URSA-111@==.com'
    str = '1h=R@-.com'

    contains_numbers, contains_alphabets_ignore_case, contains_ascii_symbols, contains_any = '(\d+)', '([a-zA-Z]+)', '([^\w]+)', '(.*)'
    is_number, is_alphabet_ignore_case, is_ascii_symbol, is_any = '(\d)', '([a-zA-Z])', '([^\w])', '(.)'

    # exactly N {N}, >= N {N,}, e.g. \d{N,}

    contains_alphabets_upper_case, contains_alphabets_lower_case = '([A-Z]+)', '([a-z]+)'
    is_alphabets_upper_case, is_alphabets_lower_case = '([A-Z])', '([a-z])'
    regex_exp = r'[\w.-]+\@[\w.-]+\.com'
    regex_exp = r'[\w.-]+\@([^\w]+)+\.com'
    regex_exp = r'([a-zA-Z]+)\@([^\w]+)+\.com'
    regex_exp = r'([a-zA-Z]+)([^\w]+)([a-zA-Z]+)\@([^\w]+)+\.com'
    regex_exp = r''+ contains_alphabets_upper_case + contains_ascii_symbols + contains_numbers +'\@' + contains_ascii_symbols +'+\.com'
    regex_exp = r'' + is_number + is_alphabet_ignore_case + is_ascii_symbol + is_alphabets_upper_case + '\@' + is_any + '+\.com'

    match = re.search(regex_exp, str)
    if match:
        print(match.group())

    str = 'URSA     --' \
          '111@=		=.com'
    str = 'URSA--' \
          '111@==.com'
    contains_newline = '[^\n]+'
    regex_exp = r'' + contains_newline

    contains_tab = '[^\t]+'
    regex_exp = r'' + contains_tab

    match = re.search(regex_exp, str, re.M)
    if match:
        print(match.group())




    print("=====[" + id_regex_lib + " End]===== \n");

    return None

####################################
## main
####################################
if __name__ == "__main__":
    regex_lib_test_00()

"""
# version: 2018-02-17_1344hr_09sec
"""