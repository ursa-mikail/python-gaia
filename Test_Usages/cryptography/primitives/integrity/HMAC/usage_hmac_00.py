import os, sys
import binascii as binascii

# point to path
lib_path = os.path.abspath('../../../../../Libraries/cryptography/primitives/integrity/HMAC')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from hmac_lib import hmac_lib	# file name
from data_formatter import data_formatter	#

# main
if __name__ == "__main__":
    data = b"140b41b22a29beb4061bda66b6747e14"
    data = b""
    key = b""
    id = "Usage Agent: <hmac>"
    print("=====[" + id + " Start]===== \n")
    hmac_object_00 = hmac_lib(id)
    hmac_byte_data_array = hmac_object_00.hmac_sha256(key, data)
    print(hmac_byte_data_array)
    print(hmac_byte_data_array[0])
    hmac_result_to_be_verified = b"an incorrect signature"

    hmac_object_01 = hmac_lib(id)
    status = hmac_object_01.hmac_sha256_verify(hmac_result_to_be_verified, key, data)
    print("Verification status: ", status)
    status = hmac_object_01.hmac_sha256_verify(hmac_byte_data_array, key, data)
    print("Verification status: ", status)


    id = "Usage Agent: <data_formatter>"
    print("=====[" + id + " Start]===== \n")
    data_formatter_object = data_formatter(id)
    operation_chosen = data_formatter_object.operation_unary_options[0] # int_to_hex string
    hex_string_array = data_formatter_object.data_conversion_on_array(hmac_byte_data_array, operation_chosen)
    print(hex_string_array)
    hex_string = ''.join(hex_string_array)
    print(hex_string)