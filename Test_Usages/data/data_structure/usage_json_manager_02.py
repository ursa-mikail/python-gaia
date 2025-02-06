####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/text')
sys.path.append(lib_path)

# import package from path
from json_manager import json_manager	# file name
#from string_processor import string_processor_class	# file name
#from text_processor import text_processor	# file name

import json
####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <json_manager>"
    print("=====[" + id + " Start]===== \n")
    json_manager_object = json_manager(id)
    json_manager_object.who_am_i()

    chart = {   "1": # depth = 0
             {
                "1.1":
                    {
                        "1.1.1": ["a", "b"],
                        "1.1.2": ["c", "d"],
                        "1.1.3": ["e", "f"],
                        "1.1.4": ["g", "h"],
                        "1.1.5": ["i", "j"],
                        "1.1.6": ["k", "l"]
                    },
                 "1.2":
                     {
                         "1.2.1": ["aa", "bb"],
                         "1.2.2":
                             {
                                 "1.2.2.1":
                                        {
                                            "1.2.2.1.1": ["see ok"],
                                        },
                                 "1.2.2.2": ["ok"],
                             },
                         "1.2.3": ["cc", "dd"],
                         "1.2.4": ["ee", "ff"]
                     },
                 "1.3":
                     {
                         "1.3.1": ["aaa", "bbb"],
                         "1.3.2": ["ccc", "ddd"],
                     },
                 "1.4":
                     {
                         "1.4.1": ["a0", "b0"],
                         "1.4.2": ["c0", "d0"],
                         "1.4.3": ["e0", "f0"],
                         "1.4.4": ["g0", "h0"],
                     },
                 "1.5":
                     {
                         "1.5.1": ["a1", "b1"],
                         "1.5.2": ["c1", "d1"],
                         "1.5.3": ["e1", "f1"],
                     },
                 "1.6":
                     {
                         "1.6.1": ["uu", "ww"],
                         "1.6.2": ["xx", "yy"],
                     }
             }
        }

    json_indented = json.dumps(chart, indent=4)
    contents_formatted_json_stream = json_manager_object.check_json_format_with_json_stream(json_indented)
    print('contents_formatted_json_stream: ', contents_formatted_json_stream)

    depth_max = json_manager_object.get_max_depth_of_json_file_structure(json_indented)
    print('depth_max: ', depth_max)

    depth_max = json_manager_object.get_depth(chart)
    print('depth_max: ', depth_max)

    layer_number_index = 3 #4
    contents = json_manager_object.extract_json_content_at_N_layer(json_indented, layer_number_index) #

    print("At level ", layer_number_index, " : ", contents, "\nLength of contents: ", len(contents))

    layer_number_index = 7
    if(json_manager_object.level_exist(json_indented, layer_number_index)):
        print("Level ", layer_number_index, " exists")
    else:
        print("Level ", layer_number_index, " exist NOT")

    number_of_keys = json_manager_object.count_number_of_keys_in_json_stream(contents)
    print('number_of_keys: ', number_of_keys)

    print(type(contents))
    contents = " ".join(contents.split("\n")) # replace newline with space
    # contents = " ".join(contents.split("\t"))  # replace tab with space
    contents = " ".join(contents.split("    "))  # replace tab with space
    keys_in_contents_serialized_string, values_in_contents_serialized_string = json_manager_object.get_keys_only_in_json_stream(contents)
    print('keys_in_contents_serialized_string: ', keys_in_contents_serialized_string)
    print('values_in_contents_serialized_string: ', values_in_contents_serialized_string)

    for i in range(0, len(values_in_contents_serialized_string)):
        print("terms: ", values_in_contents_serialized_string[i])

    print("There are ", len(values_in_contents_serialized_string), " terms")
    #contents = json_manager_object.extract_json_content_under_N_layer(json_indented, layer_number_index)
    #print("Under level ", layer_number_index, " : ", contents)

    index = '1.2.2.1'
    contents_formatted_json_stream_str = json.dumps(contents_formatted_json_stream) # str(contents_formatted_json_stream)
    # print('contents_formatted_json_stream: ', contents_formatted_json_stream_str)
    """
    #print("brace_start: ", contents[0])
    current_position = 1 # after brace_start
    position_after_brace_end = json_manager_object.search_for_position_of_end_brace_to_skip_section(contents_formatted_json_stream, current_position)
    print("position_after_brace_end: ", position_after_brace_end)
    print("brace_end: ", contents[position_after_brace_end-1])
    """
    # contents_extracted = json_manager_object.extract_json_content_under_index(contents_formatted_json_stream_str, index)

    print(contents_formatted_json_stream_str[0:15])
    print(contents_formatted_json_stream_str[14])
    index_of_brace_start = 14
    contents_extracted = json_manager_object.extract_subsection(contents_formatted_json_stream_str, index_of_brace_start)
    print(contents_extracted)

    contents_extracted = json_manager_object.extract_json_content_under_index(contents_formatted_json_stream_str, index)
    #print(contents_extracted)

    print("=====[" + id + " End]===== \n");

    """
    """

"""
# version: 2020-11-21_0400hr_20sec
"""