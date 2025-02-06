import os, sys

# point to path
lib_path = os.path.abspath('../text')
sys.path.append(lib_path)

# import package from path
from text_processor import text_processor	# file name

class lib_library_manager:
    """ Template model of Gaia """
    id = "lib_library_manager"
    id_text_processor = "Library Agent: Internal Agent <text_processor>"
    text_processor_object = text_processor(id_text_processor)

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    def get_all_functions(self, path_and_filename):  #
        """ $ echo "def encrypt_gcm(self, key, plaintext, associated_data):" | grep -o -P '(?<=def).*(?=\()'
            encrypt_gcm
        """
        function_list = []
        tag_string_front = "def "
        tag_string_behind = "("

        with open(path_and_filename) as f:
            for line in f:
                string_target = line

                if (self.text_processor_object.if_substrings_exist (string_target, [tag_string_front, tag_string_behind])):
                    function_name = self.text_processor_object.extract_string_between_tags(string_target,
                                                                                           tag_string_front,
                                                                                           tag_string_behind)
                    function_list.append(function_name)

        f.close()

        return function_list

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id_lib_library_manager = "Library Agent: Internal Agent <lib_library_manager>"
    print("=====[" + id_lib_library_manager + " Start]===== \n")
    lib_library_manager_object = lib_library_manager(id_lib_library_manager)
    file_target = "../data/file/csv_manager.py" # ""../cryptography/primitives/cipher/symmetric/aes_cipher.py"
    function_list = lib_library_manager_object.get_all_functions(file_target)
    print("function_list: ", function_list)

    # import _Gaia._gaia
    # help(lib_library_manager) # introspect

    print("=====[" + id_lib_library_manager + " End]===== \n");

"""
# version: 2017-11-23_1504hr_24sec
"""