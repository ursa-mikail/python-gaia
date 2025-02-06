####################################
import os, sys
import codecs

# point to path
lib_path = os.path.abspath('../../../../../Libraries/cryptography/primitives/key_generation/KDF/')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from KDF_lib import KDF_lib	# file name
from data_formatter import data_formatter

####################################
## main
####################################
if __name__ == "__main__":
    id_data_formatter = "Usage Agent: <data_formatter>"
    print("=====[" + id_data_formatter + " Start]===== \n")
    data_formatter_object = data_formatter(id)

    operation_unary_options = ['int_to_hex', 'hex_to_int', 'int_to_bin', 'bin_to_int',
                               'int_to_ascii', 'ascii_to_int', 'string_to_base64', 'base64_to_string',
                               'hex_to_base64', 'base64_to_hex']

    id_KDF_lib = "Usage Agent: <KDF_lib>"
    print("=====[" + id_KDF_lib + " Start]===== \n")
    KDF_lib_object = KDF_lib(id_KDF_lib)
    KDF_lib_object.who_am_i()

    operation_python_data_string_to_and_from_byte_object_options = ['string_to_bytes_object', 'bytes_object_to_string',
                                                                    'ascii_string_to_hex_string', 'hex_string_to_ascii_string',
                                                                    'ascii_bytes_object_to_hex_bytes_object', 'hex_bytes_object_to_ascii_bytes_object']

    passcode_ascii = 'secret'
    salt_ascii = 'salt'

    operation_chosen = operation_python_data_string_to_and_from_byte_object_options[0]
    passcode_ascii_bytes = data_formatter_object.data_conversion_hex_and_bytes_object(passcode_ascii, operation_chosen)
    print("passcode_ascii_bytes: ", passcode_ascii_bytes)
    operation_chosen = operation_python_data_string_to_and_from_byte_object_options[1]
    passcode_ascii_string = data_formatter_object.data_conversion_hex_and_bytes_object(passcode_ascii_bytes, operation_chosen)
    print("passcode_ascii_string: ", passcode_ascii_string)

    operation_chosen = operation_python_data_string_to_and_from_byte_object_options[2]
    passcode_hex_string = data_formatter_object.data_conversion_hex_and_bytes_object(passcode_ascii_string, operation_chosen)
    print("passcode_hex_string: ", passcode_hex_string)
    operation_chosen = operation_python_data_string_to_and_from_byte_object_options[3]
    passcode_ascii_string = data_formatter_object.data_conversion_hex_and_bytes_object(passcode_hex_string, operation_chosen)
    print("passcode_ascii_string: ", passcode_ascii_string)

    operation_chosen = operation_python_data_string_to_and_from_byte_object_options[4]
    passcode_hex_bytes = data_formatter_object.data_conversion_hex_and_bytes_object(passcode_ascii_bytes, operation_chosen)
    print("passcode_hex_bytes: ", passcode_hex_bytes)

    operation_chosen = operation_python_data_string_to_and_from_byte_object_options[5]
    passcode_ascii_bytes = data_formatter_object.data_conversion_hex_and_bytes_object(passcode_hex_bytes, operation_chosen)
    print("passcode_ascii_bytes: ", passcode_ascii_bytes)

    passcode_hex = passcode_hex_bytes.decode('ascii')
    print(passcode_hex_bytes)
    print(passcode_hex)
    passcode_hex = passcode_hex_bytes.decode('ascii')
    print(passcode_hex)
    passcode_hex_bytes = passcode_hex.encode('ascii')
    print(passcode_hex_bytes)
    # print(passcode_ascii_bytes)
    salt_ascii_bytes = salt_ascii.encode('ascii')
    salt_hex_bytes = codecs.encode(salt_ascii_bytes, 'hex')
    salt_hex = salt_hex_bytes.decode('ascii')

    salt_hex_string, number_of_iterations, sha_algorithm = salt_hex, 1000, 'sha256'
    hmac_result_hex_string = KDF_lib_object.generate_hmac_with_pbkdf2(passcode_hex_string, salt_hex_string, number_of_iterations, sha_algorithm)

    print(hmac_result_hex_string)
    hmac_in_DB = 'd2f31d6042f0436444c9b8a67e5f12fd92cd3009a393a54de2a242b224390744'

    if(KDF_lib_object.is_valid_hmac(sha_algorithm, passcode_hex_string, salt_hex_string, number_of_iterations, hmac_in_DB)):
        print("Verified")
    else:
        print("NOT Verified")


    # import _Gaia._gaia
    # help(KDF_lib) # introspect

    print("=====[" + id_KDF_lib + " End]===== \n");
