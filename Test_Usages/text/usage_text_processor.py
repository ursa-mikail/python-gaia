####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/text')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/data/file')
sys.path.append(lib_path)

# import package from path
from text_processor import text_processor	# file name
from file_manager import file_manager
'''
text processing i.e. remove empty lines, find/ substitute text, etc
'''

####################################
## main
####################################
if __name__ == "__main__":
    id_text_processor = "Test Usage Agent: <text_processor>"

    print ("=====[" + id_text_processor + " Start]===== \n")
    text_processor_object = text_processor(id_text_processor)

    statement = ' 	 		d			   	';

    line_is_empty = text_processor_object.is_empty_line(statement);
    print (line_is_empty, "\n")
    print ("Statment :\'", statement, "\' has ", len(statement), " character(s)", "\n")
    statement = text_processor_object.remove_white_spaces(statement);
    print ("Statment :\'", statement, "\' has ", len(statement), " character(s)", "\n")

    stringTarget = "          hello world    and again        hello world         ";
    print (stringTarget, "has ", len(stringTarget), " characters.\n")

    stringTarget = text_processor_object.remove_prepending_and_appending_white_spaces(stringTarget);
    print (stringTarget, "has ", len(stringTarget), " characters.\n")

    stringTarget = "          hello world    and again        hello world         ";
    stringTarget = text_processor_object.remove_prepending_white_spaces(stringTarget); # remove whitespaces before the string
    print (stringTarget, "has ", len(stringTarget), " characters.\n")

    stringTarget = text_processor_object.remove_appending_white_spaces(stringTarget); # remove whitespaces after the string
    print (stringTarget, "has ", len(stringTarget), " characters.\n")


    ## split string
    khronos_et_kairos_units_string = r' \
        Applications: Emotion tracking: `Ayahuasca` || \
        Algorithms: General || \
        Algorithms: A.I./ Machine Learning || \
        Tooling: `Gaia` || \
        Book writing: `100 Day Game` || \
        Wearables || \
        Medical || \
        Sales ||'
    # Separate on comma.
    khronos_et_kairos_units = khronos_et_kairos_units_string.split("||")

    # Loop and print each operating_unit name.
    for operating_unit in khronos_et_kairos_units:
        item = operating_unit.lstrip('\\').rstrip('\\t').rstrip('\\'),

        item = str(item)
        item = item[9:len(item)-3]

        item = text_processor_object.ensure_no_prepending_tag(item, '\t')
        item = text_processor_object.ensure_no_appending_tag(item, '\t')
        #item = operating_unit.rstrip('\\')
        #item = operating_unit[1]
        print (item)

    tag = '[test]' # '*'
    item = "[test][test][test] see - **[test][test][test]" # "******* see - *****"
    item = text_processor_object.ensure_no_prepending_tag(item, tag)
    item = text_processor_object.ensure_no_appending_tag(item, tag)
    print (item)

    string_target = "1     2     3  4   5"
    string_to_be_replaced, string_to_replaced_with = "     ", "\t" # 5 spaces, tab
    string_target_modified = text_processor_object.replace_text(string_target, string_to_be_replaced, string_to_replaced_with)
    print(string_target_modified)

    id_file_manager = "Test Usage Agent: <file_manager>"
    print("=====[" + id_file_manager + " Start]===== \n")
    file_manager_object = file_manager(id_file_manager)

    target_file = './data/view_00.txt'
    text_from_file = file_manager_object.read_file_into_string_buffer(target_file)
    print(text_from_file)

    #target_file = './data/view_00_out.txt'
    #file_manager_object.write_string_buffer_into_file(target_file, text_from_file)

    label_tag_start = '<meta-function>'
    label_tag_end = '</meta-function>'
    text_extracted = text_processor_object.extract_string_between_tags(text_from_file, label_tag_start, label_tag_end)
    print("[START]")
    print(text_extracted)
    print("[END]")

    print ("=====[" + id_text_processor + " End]===== \n")

"""
# version: 2018-01-13_2204hr_22sec
"""	