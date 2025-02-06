import os, sys
import binascii as binascii

# point to path
lib_path = os.path.abspath('../../../../../Libraries/cryptography/primitives/integrity/hash')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from sha2_lib import sha2_lib	# file name
from data_formatter import data_formatter	#

# main
if __name__ == "__main__":
    data = b"140b41b22a29beb4061bda66b6747e14"
    data = b""
    id = "Usage Agent: <sha2>"
    print("=====[" + id + " Start]===== \n")
    sha2_lib_object = sha2_lib(id)
    hash_byte_data_array = sha2_lib_object.sha256(data)
    print(hash_byte_data_array)
    print(hash_byte_data_array[0])

    id = "Usage Agent: <data_formatter>"
    print("=====[" + id + " Start]===== \n")
    data_formatter_object = data_formatter(id)
    operation_chosen = data_formatter_object.operation_unary_options[0] # int_to_hex string
    hex_string_array = data_formatter_object.data_conversion_on_array(hash_byte_data_array, operation_chosen)
    print(hex_string_array)
    operation_chosen = data_formatter_object.operation_unary_options[10]  # hex_bytes_list_to_hex_string
    hex_string = data_formatter_object.data_conversion_on_array(hex_string_array, operation_chosen)
    print(hex_string)