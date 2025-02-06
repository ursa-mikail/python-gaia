####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)

# import package from path
from dictionary_manager import dictionary_manager	# file name

# point to path
lib_path = os.path.abspath('./test_data')
sys.path.append(lib_path)

# import package from path
from data_sets import *

import collections
from pprint import pprint
####################################
## main
####################################
if __name__ == "__main__":
    id_dictionary_manager = "Library Agent: Internal Agent <dictionary_manager>"
    print("=====[" + id_dictionary_manager + " Start]===== \n")
    dictionary_manager_object = dictionary_manager(id_dictionary_manager)

    #
    data_json_root_object = collections.defaultdict(dict)
    print(data_json_root_object)

    number_of_entries = len(domain_fields)

    data_json_entry_list_object = dictionary_manager_object.initialize_dictionary_object(number_of_entries)  # node

    print(len(data_json_entry_list_object))

    for i in range(0, number_of_entries):
        node_key, node_value = 'domain_'+str(i), domain_fields[i]  # create fundamental dictionary entry item (key, value) pair
        node_child_object = dictionary_manager_object.create_dictionary_entry_object(node_key, node_value)
        node_parent_object = data_json_entry_list_object[i]
        data_json_entry_list_object[i] = dictionary_manager_object.add_dictionary_entry_to_node_object(node_parent_object, node_child_object)

        print(data_json_entry_list_object[i])

    """"""
    node_key, node_value = 'domains', data_json_entry_list_object  # create fundamental dictionary entry item (key, value) pair
    node_child_object = dictionary_manager_object.create_dictionary_entry_object(node_key, node_value)
    node_parent_object = data_json_root_object
    data_json_root_object = dictionary_manager_object.add_dictionary_entry_to_node_object(node_parent_object,
                                                                                           node_child_object)

    data_json_root_object_formatted = str(data_json_root_object).replace("defaultdict(<class 'dict'>,", "")
    data_json_root_object_formatted = data_json_root_object_formatted.replace(")", "")
    #data_json_root_object_formatted = data_json_root_object_formatted.replace('"', "")

    print(data_json_root_object_formatted)
    # pprint(data_json_root_object_formatted)

    # add node (object_list) to the root (parent node in this case) (node)
    #node_parent_object, node_children_object = data_json_root_object, data_json_entry_list_object
    #data_json_root_object = dictionary_manager_object.add_dictionary_object_list_to_object(node_parent_object, node_children_object)

    # print(data_json_root_object)


    # import _Gaia._gaia
    # help(dictionary_manager) # introspect

    print("=====[" + id_dictionary_manager + " End]===== \n");

"""
# version: 2017-11-25_2350hr_20sec
"""