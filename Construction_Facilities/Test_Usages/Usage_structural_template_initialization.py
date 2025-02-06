import sys, os
import logging

import shutil

# point to path
lib_path = os.path.abspath('../Libraries/') # e.g. ('../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from gaia_template_manager import gaia_template_manager
# from gaia_construct_main_functions import gaia_construct_main  # file name

def print_line_demarcator(title, data):
    print("============================================================")
    print("START: ", title)
    print("============================================================")
    print(data)
    print("============================================================")
    print("END: ", title)
    print("============================================================")

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

####################################
## main
####################################
if __name__ == "__main__":
    YES, NO = True, False
    RUN_FLAGS = [NO, NO, NO, YES]

    id_gaia_construct_main = "Usage Agent: <gaia_construct_main>"
    print("=====[" + id_gaia_construct_main + " Start]===== \n")
    gaia_template_manager_object = gaia_template_manager(id_gaia_construct_main)
    gaia_template_manager_object.who_am_i()

    gaia_class_name = 'test_CLASS_NAME_test'
    if (RUN_FLAGS[0] == YES):
        contents_formatted_class_file = gaia_template_manager_object.format_gaia_class_template(gaia_class_name)
        print_line_demarcator("contents_formatted_class_file", contents_formatted_class_file)

    if (RUN_FLAGS[1] == YES):
        [contents_formatted_test_usage_main, contents_formatted_test_usage_sub] = gaia_template_manager_object.format_gaia_test_usage_template(gaia_class_name)
        #print_line_demarcator("contents_formatted_test_usage_main", contents_formatted_test_usage_main)
        #print_line_demarcator("contents_formatted_test_usage_sub", contents_formatted_test_usage_sub)

    if (RUN_FLAGS[2] == YES):
        files_created = gaia_template_manager_object.create_directory_folders_and_set_templates(gaia_class_name)
        print("library_file_with_path: ", files_created[0])
        function_list = gaia_template_manager_object.list_functions(files_created[0])
        print("function_list: ", function_list)
        print("test_usage_file_with_path: ", files_created[1])
        function_list = gaia_template_manager_object.list_functions(files_created[1])
        print("function_list: ", function_list)
        print("test_usage_file_unit_test_with_path: ", files_created[2])
        function_list = gaia_template_manager_object.list_functions(files_created[2])
        print("function_list: ", function_list)



    if (RUN_FLAGS[3] == YES):
        # remove test foler
        folder_to_be_removed = './trial_areana/'

        if (os.path.exists(folder_to_be_removed)):
            try:
                # os.unlink(folder_to_be_removed)
                list_files(folder_to_be_removed)
                shutil.rmtree(folder_to_be_removed)
                print(folder_to_be_removed, " removed along with its files.")
            except OSError as error:
                logger = logging.getLogger('spam_application')
                logger.setLevel(logging.DEBUG)
                logger.error('failed, error: {0}'.format(error))
        else:
            print("<Warning>: ", folder_to_be_removed, " does not exist.")


    # import _Gaia._gaia
    # help(gaia_construct_main) # introspect

    print("=====[" + id_gaia_construct_main + " End]===== \n")

"""
# version: 2018-10-14_1135hr_10sec
"""