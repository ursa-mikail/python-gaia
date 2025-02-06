import os, sys, subprocess

# point to path
lib_path = os.path.abspath('../../Libraries/time')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/library_manager')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/text')
sys.path.append(lib_path)

# import package from path
from text_processor import text_processor	# file name

# import package from path
from timer_0 import timer_0 as timer	# file name
# from timer import timer	# file name
from lib_library_manager import lib_library_manager

class gaia_template_manager:
    """ Template model of Gaia """
    id = "gaia_template_manager"
    templates_folder = '../templates/'

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    # add other methods

    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = [];

        print("My name is Gaia [" + self.id + "].")

        return

    def format_gaia_class_template(self, gaia_class_name):
        id_timer = "Test Usage Agent: < timer >"
        print("=====[" + id_timer + " Start]===== \n")
        timer_object = timer(id_timer)

        tag_gaia_class_name = '<gaia_class>'
        tag_timestamp = '<time_stamp>'

        # access templates
        dir_to_templates = self.templates_folder
        dir_to_template_class = dir_to_templates + 'gaia_class_template.txt'
        f = open(dir_to_template_class, "r")
        contents = f.read()
        f.close()
        # now = datetime.datetime.now()
        # to do: ensure month, day, hour, minute, second if < 10 is double digit
        timestamp = timer_object.get_timestamp()
        # str(now.year) + '-' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + str(now.minute) + 'hr_' + str(now.second) + 'sec'
        contents_formatted = contents.replace(tag_gaia_class_name, gaia_class_name)
        contents_formatted = contents_formatted.replace(tag_timestamp, timestamp)

        return contents_formatted

    def format_gaia_test_usage_template(self, gaia_class_name):
        id_timer = "Test Usage Agent: < timer >"
        print("=====[" + id_timer + " Start]===== \n")
        timer_object = timer(id_timer)

        tag_gaia_class_name = '<gaia_class>'
        tag_gaia_index_starting_from_index_base_00 = '<index_starting_from_00>'
        tag_timestamp = '<time_stamp>'

        # access templates
        dir_to_templates = self.templates_folder
        dir_to_template_test_usage_main = dir_to_templates + 'gaia_test_usage_main_template.txt'
        dir_to_template_test_usage_sub = dir_to_templates + 'gaia_test_usage_sub_test_template.txt'

        # format test_main
        f = open(dir_to_template_test_usage_main, "r")
        contents = f.read()
        f.close()
        # now = datetime.datetime.now()
        # to do: ensure month, day, hour, minute, second if < 10 is double digit
        timestamp = timer_object.get_timestamp()
        # str(now.year) + '-' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + str(now.minute) + 'hr_' + str(now.second) + 'sec'

        contents_formatted = contents.replace(tag_gaia_class_name, gaia_class_name)
        contents_formatted = contents_formatted.replace(tag_gaia_index_starting_from_index_base_00, '00')
        contents_formatted_test_usage_main = contents_formatted.replace(tag_timestamp, timestamp)

        # format test_sub
        f = open(dir_to_template_test_usage_sub, "r")
        contents = f.read()
        f.close()

        timestamp = timer_object.get_timestamp()
        contents_formatted = contents.replace(tag_gaia_class_name, gaia_class_name)
        contents_formatted = contents_formatted.replace(tag_gaia_index_starting_from_index_base_00, '00')
        contents_formatted_test_usage_sub = contents_formatted.replace(tag_timestamp, timestamp)

        return [contents_formatted_test_usage_main, contents_formatted_test_usage_sub]

    def create_directory_folders_and_set_templates(self, gaia_class_name):
        # set files in [Libraries] and [Test_Usages]
        file_type = '.py'
        # hardcode the starting root path to be within 'trial_areana'
        path_start_root = '../Test_Usages/trial_areana/'
        if (os.path.exists(path_start_root)):
            pass
        else:
            os.mkdir(path_start_root)
            print(path_start_root, " created.")

        # [Libraries]
        library_path = os.path.join(path_start_root, 'Libraries/')
        library_file = 'lib_' + gaia_class_name + "." + file_type       # contents to be write to later

        if (os.path.exists(library_path)):
            print("<Warning>: ", library_path , " already exist.")
        else:
            os.mkdir(library_path)
            print(library_path, " created.")

        library_file_with_path = os.path.join(library_path, library_file)

        if (os.path.exists(library_file_with_path)):
            print("<Warning>: ", library_file_with_path , " already exist.")
        else:
            content_library = self.format_gaia_class_template(gaia_class_name)
            #os.mkdir(library_file_with_path)
            file = open(library_file_with_path, "w")
            file.write(content_library)
            file.close()
            print(library_file_with_path, " created.")


        # [Test_Usages]
        test_usage_path = os.path.join(path_start_root, 'Test_Usages/')
        test_usage_file = 'usage_' + gaia_class_name + "_main." + file_type  # contents to be write to later
        test_usage_file_unit_test = 'usage_' + gaia_class_name + "_00." + file_type # generate only 1 unit test, i.e. index 0 of N test cases

        if (os.path.exists(test_usage_path)):
            print("<Warning>: ", test_usage_path , " already exist.")
        else:
            os.mkdir(test_usage_path)
            print(test_usage_path, " created.")

        test_usage_file_with_path = os.path.join(test_usage_path, test_usage_file)
        test_usage_file_unit_test_with_path = os.path.join(test_usage_path, test_usage_file_unit_test)

        if (os.path.exists(test_usage_file_with_path)): # even if the main test usage file exist, the sub test files will not be created
            print("<Warning>: ", test_usage_file_with_path, " already exist.")
        else:
            content_test_usage_main, contents_test_usage_sub = self.format_gaia_test_usage_template(gaia_class_name)
            # os.mkdir(test_usage_file_with_path)
            file = open(test_usage_file_with_path, "w")
            file.write(content_test_usage_main)
            file.close()
            print(test_usage_file_with_path, " created.")

            # create unit test file
            file = open(test_usage_file_unit_test_with_path, "w")
            file.write(contents_test_usage_sub)
            file.close()
            print(test_usage_file_unit_test_with_path, " created.")

        files_created = [library_file_with_path, test_usage_file_with_path, test_usage_file_unit_test_with_path]

        return files_created

    def list_functions(self, path_to_py_file):
        id_lib_library_manager = "Library Agent: Internal Agent <lib_library_manager>"
        # print("=====[" + id_lib_library_manager + " Start]===== \n")
        lib_library_manager_object = lib_library_manager(id_lib_library_manager)
        # file_target = "../data/file/csv_manager.py"  # ""../cryptography/primitives/cipher/symmetric/aes_cipher.py"
        file_target = path_to_py_file
        function_list = lib_library_manager_object.get_all_functions(file_target)
        # print("function_list: ", function_list)

        return function_list


    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <gaia_template_manager>"
    print("=====[" + id + " Start]===== \n")
    gaia_template_manager_object = gaia_template_manager(id)
    gaia_template_manager_object.who_am_i()

    gaia_class_name = 'test'
    contents_formatted = gaia_template_manager_object.format_gaia_class_template(gaia_class_name)

    print("contents_formatted: ", contents_formatted)

    # import _Gaia._gaia
    # help(gaia_template_manager) # introspect

    print("=====[" + id + " End]===== \n");

"""
Notes: write to file target to be coded

# version: 2018-05-14_2014hr_34sec
"""