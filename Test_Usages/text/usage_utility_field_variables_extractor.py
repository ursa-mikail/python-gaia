####################################
import os, sys, re
from re import finditer

# point to path
lib_path = os.path.abspath('../../Libraries/text')
sys.path.append(lib_path)
# point to path
lib_path = os.path.abspath('../../Utilities/text')
sys.path.append(lib_path)

# import package from path
from text_processor import text_processor	# file name
from field_variables_extractor import field_variables_extractor	# file name


def read_file(path_to_file):
    contents = []
    try:
        with open(path_to_file) as fp:
            line = fp.readline()
            contents.append(line)
            cnt = 1
            while line:
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                contents.append(line)
                cnt += 1
    finally:
        fp.close()

    return contents

####################################
## main
####################################
if __name__ == "__main__":
    id = "Test Usage Agent: Internal Agent <utility field_variables_extractor>"
    print ("=====[" + id + " Start]===== \n")
    field_variables_extractor_object = field_variables_extractor(id)
    field_variables_extractor_object.who_am_i()

    start, end = '\(', '\)'
    # start, end = '\[', '\]'
    # start, end = 'see', 'me'
    line = "-(123) = (45(test)6) = (789)- [123] + [455] **** [ok] see iii me see mmm me"
    items_found = field_variables_extractor_object.text_processor_object.find_multiple_occurrences_of_string_between_tags_with_embedded_contents(line, start, end)
    print(items_found)

    path_to_file = './data/owners.txt'
    contents = read_file(path_to_file)
    print('contents: ', contents)
    user_ids = field_variables_extractor_object.get_user_ids(contents)

    user_ids = list(set(user_ids))
    user_ids = sorted(user_ids)
    print(user_ids)
    print(len(user_ids))

    email_addresses = field_variables_extractor_object.get_email_addresses(contents)
    email_addresses = list(set(email_addresses))
    email_addresses = sorted(email_addresses)
    print(email_addresses)
    print(len(email_addresses))

    contents_str = ''.join(contents)
    print(contents_str)
    date_time = field_variables_extractor_object.get_date_time(contents_str)
    date_time = list(set(date_time))
    date_time = sorted(date_time)
    print(date_time)
    print(len(date_time))

    ip_addresses = field_variables_extractor_object.get_ip_addresses(contents_str)
    print(ip_addresses)
    print(len(ip_addresses))

    hex_values = field_variables_extractor_object.get_hex_values(contents_str)
    print(hex_values)
    print(len(hex_values))

    binary_values = field_variables_extractor_object.get_binary_values(contents_str)
    print(binary_values)
    print(len(binary_values))

    file_url_path = field_variables_extractor_object.get_file_url_path(contents_str)
    print(file_url_path)
    print(len(file_url_path))

    print('=========================================================================')

    target_string = 'a1b2abcde0c3d4'
    regex_pattern = "[a-z]"
    p = re.compile(regex_pattern)
    for m in p.finditer(target_string):
        print(m.start(), m.group())
        print(m.span())


    number_of_characters_for_month, number_of_characters_for_day = 2, 2
    demarcator = ':=[\].-'
    space_or_no_space = '\s+' # '[ ]?' # [ \t\n]+
    target_string = 'Day 110 :      [08.10] text .... '
    target_string = '     Day 110 :      [2019-08-10] text .... '
    target_string = '     Day 110 :      [2019-08-10] text .... Day 111: [2019-08.11] .... test 2 ...'
    # ^(?=.*\d).{6,20}$ # for 6 to 20 numbers
    regex_pattern = r'Day .*[0-9].*[' + demarcator + ']\d{' + str(number_of_characters_for_month) + \
                    '}[' + demarcator + ']\d{' + str(number_of_characters_for_day) + '}[' + demarcator + ']'
    regex_pattern = r'Day .*[0-9].*[' + demarcator + ']' + space_or_no_space + '[' + demarcator + ']' + \
        '(?=.*\d).{0,4}' + '[' + demarcator + ']?' + '(?=.*\d).{2,2}' + \
        '[' + demarcator + ']' + '(?=.*\d).{2,2}' + '[' + demarcator + ']'

    p = re.compile(regex_pattern)
    for m in p.finditer(target_string):
        print(m.start(), m.group())

    m = p.search(target_string)
    print(m.start(), m.group())
    print(m.span())

    print('=========================================================================')
    for match in finditer(regex_pattern, target_string):
        print(match.span(), match.group())

    # print(contents_str)
    print('=========================================================================')

    regex_pattern = "Day .*: \[.*\]"
    regex_pattern = "Day .*: \[.*\]\s+\(.*\)"
    #filename = "./input"
    filename = path_to_file;
    lines = [line.rstrip('\n') for line in open(filename)]
    #lines = target_string;

    result = {}
    prev_delimiter = ""
    for line in lines:
        # print("line: ", line)
        splitArr = re.split(regex_pattern, line)
        delimiter = re.findall(regex_pattern, line)
        # print("delimiter: ", delimiter)
        if len(delimiter) > 0 and len(delimiter[0]) > 0:
            prev_delimiter = delimiter[0]
            # print("prev_delim: ", prev_delimiter)
            if delimiter[0] in result.keys():
                result[delimiter[0]] = result[delimiter[0]].append(splitArr)
            else:
                result[delimiter[0]] = splitArr
        else:
            # print("here, prev_delim: ", prev_delimiter)
            # print("here, result[p_d]: ", result[prev_delimiter])
            if prev_delimiter in result.keys() and len(splitArr[0]) > 0:
                result[prev_delimiter].append(splitArr[0])
    # for key, val in result.items():
    #   result[key] = "".join(val)
    print("result: \n\n\n")
    print(result)

    for key, value in result.items():
        print(key + '    >>   ' + str(value))

    print('=========================================================================')
    """
    Strings_To_Search = ['https://projects.lukehaas.me/regexhub/',
                         'C://path/folder_0/file',
                         'c://path/folder_0/file',
                         'www.google.com',
                         'www.test.com/123/456']

    for url in Strings_To_Search:
        if re.findall(r'^(https|http|www)', url):
            print('Found URL: ' + url)
        elif re.findall(r'(\w{1}:)', url):
            print('Found File Path: ' + url)
    """
    print ("=====[" + id + " End]===== \n")

"""
# version: 2019-07-27_2151hr_33sec
"""