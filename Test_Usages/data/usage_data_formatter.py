####################################
import os, sys


# point to path
lib_path = os.path.abspath('../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/cryptography/primitives/cipher/symmetric')
sys.path.append(lib_path)

# import package from path
from data_formatter import data_formatter	# file name
from padding_schemes import padding_schemes

####################################
## main
####################################
if __name__ == "__main__":
    id = "Usage Agent: <data_formatter>"
    print ("=====[" + id + " Start]===== \n")
    data_formatter_object = data_formatter(id)
    data_formatter_object.who_am_i()

    operation_chosen = data_formatter_object.operation_unary_options[0]

    int_bytes = [10, 255, 0, 16, 15, 9999245524, 1885435244]
    hex_string_array = data_formatter_object.data_conversion_on_array(int_bytes, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", hex_string_array)

    operation_chosen = data_formatter_object.operation_unary_options[1]

    int_array = data_formatter_object.data_conversion_on_array(hex_string_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", int_array)

    operation_chosen = data_formatter_object.operation_unary_options[2]

    binary_array = data_formatter_object.data_conversion_on_array(int_bytes, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", binary_array)

    operation_chosen = data_formatter_object.operation_unary_options[3]

    int_array_01 = data_formatter_object.data_conversion_on_array(binary_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", int_array_01)

    operation_chosen = data_formatter_object.operation_unary_options[4]

    ascii_array = data_formatter_object.data_conversion_on_array(int_bytes, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", ascii_array)

    operation_chosen = data_formatter_object.operation_unary_options[5]

    int_bytes_02 = data_formatter_object.data_conversion_on_array(ascii_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", int_bytes_02)

    operation_chosen = data_formatter_object.operation_unary_options[6]

    string_array = ['quick brown', ' fox jumps over ', 'the lazy dog']
    base64_array = data_formatter_object.data_conversion_on_array(string_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", base64_array)

    operation_chosen = data_formatter_object.operation_unary_options[7]

    string_array_01 = data_formatter_object.data_conversion_on_array(base64_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", string_array_01)

    operation_chosen = data_formatter_object.operation_unary_options[8]
    hex_string_array = ['10000000000002ae', '10000000000002ff']
    base64_array = data_formatter_object.data_conversion_on_array(hex_string_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", base64_array)

    operation_chosen = data_formatter_object.operation_unary_options[9]
    hex_array_03 = data_formatter_object.data_conversion_on_array(base64_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", hex_array_03)

    operation_chosen = data_formatter_object.operation_unary_options[8]
    base64_array = data_formatter_object.data_conversion_on_array(hex_array_03, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", base64_array)

    operation_chosen = data_formatter_object.operation_unary_options[9]
    base64_string = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw4ZQ2SnyomhimNv+IlX0plel0G3K1iPS5WVmIcI/YPWroQWPBKVGcYfSJdkuZn/Rdc+BslzAYX+N0pJXwZlzAKTcSi+y5u41LLtXKJDawDFRXYPC3pXJg9YFnl0VFFjjzUet2LsIXVN7bEUoAE7i/HFF2+QF5BakEP0GVOHzMTvILyHASKbSSjNrYjUJ28Z/cKvWuBFn2yyVBgKC1duVpbUDWHdnuqG27XX/yb9kz+ndTp7QNziLiuMDrYmkw21Y17Sduj5Nu5U8Rhlz9AQcEBGbZQ7VnYxK9fqlB2NPMBHY+r3afpmzrcDDfI8ckIPrO2jW0m2pVD8quMxxJeihZQIDAQAB"
    base64_array = [base64_string]
    hex_array_04 = data_formatter_object.data_conversion_on_array(base64_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", hex_array_04)

    operation_chosen = data_formatter_object.operation_unary_options[8]
    base64_array_00 = data_formatter_object.data_conversion_on_array(hex_array_04, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", base64_array_00)

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[0]
    string_target = 'test'
    byte_object = data_formatter_object.data_conversion_hex_and_bytes_object(string_target, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", byte_object[0])

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[1]
    string_result = data_formatter_object.data_conversion_hex_and_bytes_object(byte_object, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", string_result)

    # commonly used for cipher inputs
    operation_chosen = data_formatter_object.operation_unary_options[0]
    byte_data_array = [104, 101, 108, 108, 111, 226, 157, 164]
    print("operation_chosen: ", operation_chosen, "\n byte_data_array: ", byte_data_array)  # integer array
    hex_data_array = data_formatter_object.data_conversion_on_array (byte_data_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n hex_data_array: ", hex_data_array)   # integer array to hex characters

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[6]
    byte_object = data_formatter_object.data_conversion_hex_and_bytes_object(byte_data_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", byte_object[1])
    print("operation_chosen: ", operation_chosen, "\n byte_object: ", byte_object)         # integer array to binary object

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[7]
    string_target = data_formatter_object.data_conversion_hex_and_bytes_object(byte_object, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n string_target: ", string_target)     # binary object to string

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[8]
    byte_object_00 = data_formatter_object.data_conversion_hex_and_bytes_object(string_target, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n byte_object (string to byte array / object): ", byte_object_00)  # string to binary object

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[9]
    int_array = data_formatter_object.data_conversion_hex_and_bytes_object(byte_object_00, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n int_array: ", int_array)  # binary object to integer array

    operation_chosen = data_formatter_object.operation_unary_options[0]
    hex_data_array = data_formatter_object.data_conversion_on_array(byte_object_00, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n binary object to hex_data_array: ", hex_data_array)  # binary object to hex characters

    operation_chosen = data_formatter_object.operation_unary_options[1]
    int_array_00 = data_formatter_object.data_conversion_on_array(hex_data_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n hex_data_array to integer array: ", int_array_00)  # hex characters to integer array


    byte_object_00 = b'hello\xe2\x9d\xa4' # equivalent to byte_data_array
    print(byte_object_00[0])
    print(len(byte_object_00))
    print(byte_object_00)

    operation_chosen = data_formatter_object.operation_unary_options[4]
    ascii_array = data_formatter_object.data_conversion_on_array (byte_data_array, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n resultant: ", ascii_array)

    #operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[7]
    #byte_object_01 = data_formatter_object.data_conversion_hex_and_bytes_object(ascii_array, operation_chosen)
    #print(byte_object_01)

    import string
    number_of_alphabets = 26
    # numbers = list(range(0, 9))
    string_list = string.ascii_lowercase[:number_of_alphabets] + string.ascii_uppercase[:number_of_alphabets]
    print("string_list: " + string_list)

    length_of_cipher = 16
    length_of_string = number_of_alphabets

    id = "Usage Agent: <padding_schemes>"
    print("=====[" + id + " Start]===== \n")
    padding_schemes_object = padding_schemes(id)
    padding_schemes_object.who_am_i()

    data_string = string_list[0:length_of_string]
    print("data_string: ", data_string)

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[8]
    byte_object_00 = data_formatter_object.data_conversion_hex_and_bytes_object(data_string, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n byte_object (string to byte array / object): ", byte_object_00)  # string to binary object

    operation_chosen = data_formatter_object.operation_python_data_string_to_and_from_byte_object_options[9]
    int_array_00 = data_formatter_object.data_conversion_hex_and_bytes_object(byte_object_00, operation_chosen)
    print("operation_chosen: ", operation_chosen, "\n int_array: ", int_array_00)  # binary object to integer array

    block_length = length_of_cipher
    data_int_array_padded_00 = padding_schemes_object.PKCS7_on_int_array(int_array_00, block_length)
    print("operation_chosen: ", operation_chosen, "\n data_int_array_padded_00: ", data_int_array_padded_00)

    data_int_array_padded_01 = padding_schemes_object.padding_zero_with_x80h_at_front_on_int_array(int_array_00, block_length)
    print("data_int_array_padded_01: ", data_int_array_padded_01)
    # print("int_array: ", int_array_00)

    data_int_array_padded_02 = padding_schemes_object.padding_zero_with_length_of_pad_at_end_on_int_array(int_array_00, block_length)
    print("data_int_array_padded_02: ", data_int_array_padded_02)

    data_int_array_padded_03 = padding_schemes_object.padding_zero_on_int_array(int_array_00, block_length)
    print("data_int_array_padded_03: ", data_int_array_padded_03)

    data_int_array_padded_04 = padding_schemes_object.padding_with_space_x20h_on_int_array(int_array_00, block_length)
    print("data_int_array_padded_04: ", data_int_array_padded_04)

    data_int_array_padded_05 = padding_schemes_object.padding_random_on_int_array(int_array_00, block_length)
    print("data_int_array_padded_05: ", data_int_array_padded_05)

    data_int_array_padded_06 = padding_schemes_object.padding_random_with_length_of_pad_at_end_on_int_array(int_array_00, block_length)
    print("data_int_array_padded_06: ", data_int_array_padded_06)

    print ("=====[" + id + " End]===== \n")

"""
# version: 2018-04-04_1949hr_49sec
"""	