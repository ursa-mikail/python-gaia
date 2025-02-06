'''
Utility: Gaia templates generator to create modules that includes library module, test usage, and utility codes.
'''
####################################
import os, sys
import re
import datetime

# point to path
lib_path = os.path.abspath('./Libraries/')
sys.path.append(lib_path)

# import package from path
from gaia_template_manager import gaia_template_manager as gaia_template_manager

# point to path
lib_path = os.path.abspath('../Libraries/Lib_00')
sys.path.append(lib_path)

# import package from path
import _lib;	# file name



####################################
## main
####################################
if __name__ == "__main__":
    id = "Utility Agent: < utility_Gaia_generate_templates >"
    print ("=====[" + id + " Start]===== \n");
    _gaia_object = _lib._lib_class(id); # file_name.class_name
    number_of_lines = _gaia_object.who_am_i();

    """
    id_timer = "Test Usage Agent: < timer >"
    print("=====[" + id_timer + " Start]===== \n")
    timer_object = timer(id_timer)
    """
    id = "Library Agent: Internal Agent <gaia_template_manager>"
    print("=====[" + id + " Start]===== \n")
    gaia_template_manager_object = gaia_template_manager(id)
    gaia_template_manager_object.who_am_i()

    path_library = input("Create dir from given library path at dir: Gaia/Libraries/Lib_<index>/object/object_function/, \n \
                            e.g. dir: Gaia/Libraries/Lib_01/text/checker/ \n \
                            e.g. input: Lib_xx/text/checker :  \n  ")
    print("To make: " + path_library + "!")

    currentFile = __file__  # May be 'my_script', or './my_script' or
                        # '/home/user/test/my_script.py' depending on exactly how
                        # the script was run/loaded.
    fullPath = os.path.realpath(currentFile)  # /home/user/test/my_script.py
    dirPath = os.path.dirname(fullPath)  # /home/user/test
    dirName = os.path.basename(dirPath) # test

    print("currentFile: " + currentFile)
    print("fullPath: " + fullPath)
    print("dirPath: " + dirPath)
    print("dirName: " + dirName)

    path_home = os.path.expanduser('~')

    print("path_home: " + path_home)

    # find common prefix
    print (os.path.commonprefix(['/usr/var/log', '/usr/var/security']))

    path_to_Gaia = '/PycharmProjects/Ursa/ayahuasca/gaia/'
    path_to_Gaia_full = path_home + path_to_Gaia
    path_to_Gaia_full_libraries = path_to_Gaia_full + 'Libraries/'
    path_to_Gaia_full_test_usages = path_to_Gaia_full + 'Test_Usages/'

    path_to_Gaia_full_library_new = path_to_Gaia_full_libraries + path_library
    path_to_Gaia_full_test_usage_new = path_to_Gaia_full_test_usages + path_library
    print("path_to_Gaia_full_library_new : ", path_to_Gaia_full_library_new)
    print("path_to_Gaia_full_test_usage_new : ", path_to_Gaia_full_test_usage_new)

    gaia_class_name = re.split('\\/',path_library)
    print("gaia_class_name: ", gaia_class_name)
    gaia_class_name = gaia_class_name[len(gaia_class_name) - 1] # get the last item
    print("gaia_class_name: ", gaia_class_name)

    #contents_formatted = gaia_template_manager_object.format_gaia_class_template(gaia_class_name)
    #print("contents_formatted: \n", contents_formatted)

    [contents_formatted_test_usage_main, contents_formatted_test_usage_sub] = gaia_template_manager_object.format_gaia_test_usage_template(gaia_class_name)
    print("contents_formatted_test_usage_main: \n ============================== \n", contents_formatted_test_usage_main)
    print("contents_formatted_test_usage_sub: \n ============================== \n", contents_formatted_test_usage_sub)
    print("============================== \n")

    print ("=====[" + id + " End]===== \n")


"""
= create a python module to create do initial setup for the framework for programming library module within dir:Gaia/Utility/
# Library template creation
# create dir from given library path at dir:Gaia/Libraries/Lib_<index>/object/object_function/, e.g. dir:Gaia/Libraries/Lib_01/text/checker/
# copy template from dir:Gaia/Utility/templates/codes/ to library path and rename according to given library module name as<action_object>.py, e.g. checking_parameter.py
# emend class name of library
e.g. 
<sample_code>
class checking_parameter_class:
:
if __name__ == "__main__":
    id = "Internal Agent: <checking_parameter>"
    print ("=====[" + id + " Start]===== \n")
    checking_parameter_object = checking_parameter_class(id)
    checking_parameter_object.who_am_i()
    print ("=====[" + id + " End]===== \n");
</sample_code>

# auto run test simple local run: clr; py3 checking_parameter.py;
# Test usage template creation
# create dir from given test usage path at dir:Gaia/Test_Usages/Lib_<index>/object/object_function/, e.g. dir:Gaia/Test_Usages/Lib_01/text/checker/
# copy template from dir:Gaia/Utility/templates/codes/ to test usage path and rename according to given library module name as<action_object>.py, e.g. usage_checking_parameter.py
# emend path header pointing to use the library
e.g. 
<sample_code>
# point to path
lib_path = os.path.abspath('../../Lib_01/text/checker')
sys.path.append(lib_path)

# import package from path
import checking_parameter	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id = "Test Usage Agent: <checking_parameter>"
    print ("=====[" + id + " Start]===== \n")
    checking_parameter_object = checking_parameter_class(id)
    checking_parameter_object.who_am_i()
    print ("=====[" + id + " End]===== \n");
</sample_code>

# auto run test simple library call run: clr; py3 usage_checking_parameter.py
# Utility template creation
# create dir from given test usage path at dir:Gaia/Utilities/Lib_<index>/object/object_function/, e.g. dir:Gaia/Utilities/Lib_01/text/checker/
# copy template from dir:Gaia/Utility/templates/codes/ to test usage path and rename according to given library module name as<action_object>.py, e.g. utility_checking_parameter.py
# emend path header pointing to use the library
e.g. 
<sample_code>
# point to path
lib_path = os.path.abspath('../../Lib_01/text/checker')
sys.path.append(lib_path)

# import package from path
import checking_parameter	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id = "Utility Agent: <checking_parameter>"
    print ("=====[" + id + " Start]===== \n")
    checking_parameter_object = checking_parameter_class(id)
    checking_parameter_object.who_am_i()
    print ("=====[" + id + " End]===== \n");

# auto run test simple library call run: clr; py3 utility_checking_parameter.py

</sample_code>
"""

"""
    2018-05-14_2023hr_31sec
"""