import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/library_manager')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/text') # library_manager uses text
sys.path.append(lib_path)

# import package from path
from lib_library_manager import lib_library_manager	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id_lib_library_manager = "Test Usage Agent: <lib_library_manager>"
    print("=====[" + id_lib_library_manager + " Start]===== \n")
    lib_library_manager_object = lib_library_manager(id_lib_library_manager)
    file_target = "../../Libraries/cryptography/primitives/cipher/symmetric/aes_cipher.py"
    function_list = lib_library_manager_object.get_all_functions(file_target)
    print("function_list: ", function_list)

    # import _Gaia._gaia
    # help(lib_library_manager) # introspect

    print("=====[" + id_lib_library_manager + " End]===== \n");

"""
# version: 2017-11-23_1504hr_24sec
"""