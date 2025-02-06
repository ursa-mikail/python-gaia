import os, sys
import binascii as binascii

# point to path
lib_path = os.path.abspath('../../../../../Libraries/cryptography/primitives/cipher/symmetric')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../../Libraries/data/file')
sys.path.append(lib_path)


# import package from path
from aes_cipher import aes_cipher	# file name
from data_formatter import data_formatter
from file_manager import file_manager	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id_aes_cipher = "Usage Agent: <aes_cipher>"
    print("=====[" + id_aes_cipher + " Start]===== \n")
    aes_cipher_object = aes_cipher(id_aes_cipher)

    id_data_formatter = "Usage Agent: <data_formatter>"
    print("=====[" + id_data_formatter + " Start]===== \n")
    data_formatter_object = data_formatter(id_data_formatter)

    byte_data_array_00 = [104, 101, 108, 108, 111, 226, 157, 164]
    byte_object_00 = b'hello\xe2\x9d\xa4'  # equivalent to byte_data_array_00
    print(byte_object_00[0])
    print(len(byte_object_00))

    operation_chosen = data_formatter_object.operation_unary_options[4]
    ascii_array = data_formatter_object.data_conversion_on_array(byte_data_array_00, operation_chosen)
    print(ascii_array)

    id_file_manager = "Usage Agent: <file_manager>"
    print("=====[" + id_file_manager + " Start]===== \n")
    file_manager_object = file_manager(id_file_manager)
    file_manager_object.who_am_i()

    in_filename = "./test_data/101.txt"
    file_size = file_manager_object.get_file_size(in_filename)
    print("file_size: ", file_size, " bytes.")

    file_in_byte_array = file_manager_object.read_file_into_byte_array(in_filename)
    print(file_in_byte_array)
    print(file_in_byte_array[0])

    # ===================================================
    # GCM
    # ===================================================
    number_of_bytes = 16
    key = aes_cipher_object.generate_nonce(number_of_bytes)
    print(key)
    print(type(key))

    associated_data = b"crossing technological singularity era" # b"authenticated but not encrypted payload"
    number_of_bytes_associated_data = len(associated_data)
    print("number_of_bytes_associated_data: ", number_of_bytes_associated_data)

    iv, ciphertext, tag = aes_cipher_object.encrypt_gcm( key,
        file_in_byte_array, # b"a secret message!",
        associated_data
    )

    file_in_byte_array_ciphered = ciphertext
    file_in_byte_array_deciphered = aes_cipher_object.decrypt_gcm(key, associated_data, iv, file_in_byte_array_ciphered, tag)

    print(file_in_byte_array_deciphered)

    out_filename = "./test_data/101_out.txt"
    file_manager_object.write_byte_array_into_file(out_filename, file_in_byte_array_deciphered)


"""
# version: 2018-03-24_1111_11sec
"""
