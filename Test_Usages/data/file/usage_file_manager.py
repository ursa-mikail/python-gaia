import os, sys


# point to path
lib_path = os.path.abspath('../../../Libraries/data/file')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/cryptography/primitives/integrity/hash')
sys.path.append(lib_path)

# import package from path
from file_manager import file_manager	# file name
from data_formatter import data_formatter
from sha2_lib import sha2_lib

####################################
## main
####################################
if __name__ == "__main__":
    id_file_manager = "Usage Agent: Internal Agent <file_manager>"
    print("=====[" + id_file_manager + " Start]===== \n")
    file_manager_object = file_manager(id_file_manager)
    file_manager_object.who_am_i()

    in_filename = "./test_data/101.pdf"
    file_size = file_manager_object.get_file_size(in_filename)
    print("file_size: ", file_size, " bytes.")

    [time_created, time_last_accessed, time_last_modified, time_last_changed] = file_manager_object.get_file_activity_times(in_filename)
    print([time_created, time_last_accessed, time_last_modified, time_last_changed])

    print(file_manager_object.get_file_owner_name(in_filename))

    file_in_byte_array = file_manager_object.read_file_into_byte_array(in_filename)
    print(file_in_byte_array)
    print(file_in_byte_array[0])

    id = "Usage Agent: <sha2>"
    print("=====[" + id + " Start]===== \n")
    sha2_lib_object = sha2_lib(id)
    hash_byte_data_array = sha2_lib_object.sha256(file_in_byte_array)
    #hash_byte_data_array = sha2_lib_object.sha384(file_in_byte_array)
    #hash_byte_data_array = sha2_lib_object.sha512(file_in_byte_array)

    id = "Usage Agent: <data_formatter>"
    print("=====[" + id + " Start]===== \n")
    data_formatter_object = data_formatter(id)
    operation_chosen = data_formatter_object.operation_unary_options[0]  # int_to_hex string
    hex_string_array = data_formatter_object.data_conversion_on_array(hash_byte_data_array, operation_chosen)
    print(hex_string_array)
    operation_chosen = data_formatter_object.operation_unary_options[10]  # hex_bytes_list_to_hex_string
    hex_string = data_formatter_object.data_conversion_on_array(hex_string_array, operation_chosen)
    print(hex_string)
    print("sha256 of file : ", hex_string)


    hex_string = file_manager_object.read_file_into_hex_string(in_filename)
    print(hex_string)
    out_filename = "./test_data/101_out.pdf"
    # file_manager_object.write_hex_string_into_file(out_filename, hex_string)
    file_manager_object.write_byte_array_into_file(out_filename, file_in_byte_array)

    files_with_paths = [out_filename]
    #zip_file_name = "./test_data/101_out.pdf.tar.gz"
    zip_file_name = "./test_data/101_out.pdf.zip"
    file_manager_object.zip_files(files_with_paths, zip_file_name)
    # file_manager_object.tar_files(files_with_paths, zip_file_name)

    zip_extract_path = "./test_data/test_data_00/"
    file_manager_object.extract_zip_file(zip_extract_path, zip_file_name)

    [zip_files_list, zip_files_compression_ratio] = file_manager_object.read_zip_file_list(zip_file_name)
    print("zip_files_compression_ratio = ", zip_files_compression_ratio)
    print("zip_files_list = ", zip_files_list)


    #
    paths = ['/home/user1/tmp/coverage/test', '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members']
    # paths = ['/home/useXr1/tmp/coverage/test', '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members']
    common_path = file_manager_object.get_common_path(paths)

    print("common_path: ", common_path)

    target_dir = './test_data/'
    os.chdir(target_dir)
    # print(os.listdir())
    file_type = '.zip'
    print('Get all ', file_type, ' :')
    for filename in os.listdir():
        if filename.endswith(file_type):
            # os.unlink(filename)
            print(filename)

    os.chdir('../')
    totalSize = 0
    for filename in os.listdir(target_dir):
        totalSize = totalSize + os.path.getsize(os.path.join(target_dir, filename))
    print("totalSize: ", totalSize, " bytes")

    path_to_file = 'C:\\Windows\\System32\\calc.exe'
    print(os.path.basename(path_to_file))
    print(os.path.dirname(path_to_file))

    # use this for pathing: os.path.join('usr', 'bin', 'spam')

    """
    -os.unlink(path) will delete the file at path.
    -os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
    -shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
    """

    # import _Gaia._gaia
    # help(file_manager) # introspect

    print("=====[" + id_file_manager + " End]===== \n");
