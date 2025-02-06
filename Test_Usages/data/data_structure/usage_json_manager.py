####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)

# import package from path
from json_manager import json_manager	# file name

import json
####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <json_manager>"
    print("=====[" + id + " Start]===== \n")
    json_manager_object = json_manager(id)
    json_manager_object.who_am_i()

    json_file = ['./test_data/in_0.json', './test_data/in_1.json', './test_data/in_0.json', './test_data/out_0.json']
    file_json_chosen = json_file[1]
    contents_formatted = open(file_json_chosen).read()
    # print (contents_formatted)

    contents_serialized = json.loads(contents_formatted)
    print(type(contents_serialized))
    contents_serialized_string = str(contents_serialized)   # <class 'dict'> to str
    max_depth = json_manager_object.get_max_depth_of_json_file_structure(contents_serialized_string)
    print("\n\nThe maximal depth is:" + str(max_depth))

    layer_number_index = 2

    content_extracted = json_manager_object.extract_json_content_at_N_layer(contents_serialized_string,
                                                                                   layer_number_index)
    print("\n\ncontent_extracted:")
    print(content_extracted)

    layer_number_index = 0

    content_extracted = json_manager_object.extract_json_content_under_N_layer(contents_serialized_string,
                                                                                      layer_number_index)
    print("\n\ncontent_extracted:")
    print(content_extracted)

    # import _Gaia._gaia
    # help(json_manager) # introspect

    file_json_chosen = json_file[2]
    print("file_json_chosen: ", file_json_chosen)
    #json_file_data = json_manager_object.load_json_data_from_file(file_json_chosen)
    #print(json_file_data)
    #file_json_chosen = json_file[3]
    #json_manager_object.write_json_data_to_file(json_file_data, file_json_chosen)


    # json format checker
    json_files_valid, json_files_invalid = [], []
    path_to_json_samples = './test_data/'
    files_json = ['good.json', 'bad.json']

    file_json_chosen = path_to_json_samples + files_json[1]
    print(file_json_chosen)
    contents_formatted = open(file_json_chosen).read()
    # print("contents_formatted: ", contents_formatted)
    contents_formatted_json_stream = json_manager_object.check_json_format_with_json_stream(contents_formatted)
    print("contents_formatted_json_stream: ", contents_formatted_json_stream)

    json_stream = json_manager_object.check_json_format_with_json_file(file_json_chosen)
    print("json_stream: ", json_stream)

    file_00 = path_to_json_samples + files_json[0]
    file_01 = path_to_json_samples + files_json[1]
    files_json_with_path = [file_00, file_01]
    json_files_valid, json_files_invalid = json_manager_object.check_json_format(files_json_with_path)
    print("json_files_valid: ", json_files_valid)
    print("json_files_invalid: ", json_files_invalid)

    print("=====[" + id + " End]===== \n");

"""
# version: 2017-11-25_2350hr_20sec
"""