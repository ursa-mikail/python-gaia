# import < import_packages>
import copy
import secrets # for Cryptographically Secure Random Numbers

class padding_schemes:
    """  """
    id = "padding_schemes"

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    # on integer array
    def PKCS7_on_int_array (self, data_int_array, block_length): # padding_PKCS5 # PKCS7
        # data_padded = data_int_array
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        # padding_PKCS5 # PKCS7
        data_to_pad_with = number_of_bytes_to_pad # hex(number_of_bytes_to_pad) // str

        for i in range(0, number_of_bytes_to_pad):
            data_padded.append(data_to_pad_with)

        return data_padded

    def padding_zero_with_x80h_at_front_on_int_array (self, data_int_array, block_length): # ISO/IEC 7816-4
        # data_padded = data_int_array
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        data_padded.append(int("80", 16))    # ‘80’ in hex)

        for i in range(0, (number_of_bytes_to_pad-1)):
            data_padded.append(0)

        return data_padded

    def padding_zero_with_length_of_pad_at_end_on_int_array (self, data_int_array, block_length): # ANSI X.923
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        for i in range(0, (number_of_bytes_to_pad - 1)):
            data_padded.append(0)

        data_padded.append(number_of_bytes_to_pad)  # last byte = number of padding bytes

        return data_padded

    def padding_zero_on_int_array (self, data_int_array, block_length): # ANSI X.923
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        for i in range(0, number_of_bytes_to_pad):
            data_padded.append(0)

        return data_padded

    def padding_with_space_x20h_on_int_array (self, data_int_array, block_length): # ANSI X.923
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        for i in range(0, number_of_bytes_to_pad ):
            data_padded.append(int("20", 16))  # ‘20’ in hex)

        return data_padded

    def padding_random_on_int_array (self, data_int_array, block_length): # ANSI X.923
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        lower_bound, upper_bound = 0, 256
        
        for i in range(0, number_of_bytes_to_pad):
            random_number = lower_bound + secrets.randbelow(upper_bound)
            data_padded.append(random_number)  # random_hex

        return data_padded

    def padding_random_with_length_of_pad_at_end_on_int_array(self, data_int_array, block_length):  # ISO 10126
        data_padded = copy.copy(data_int_array)
        number_of_bytes_to_pad = len(data_int_array) % block_length
        number_of_bytes_to_pad = block_length - number_of_bytes_to_pad  # if 0, add another block

        lower_bound, upper_bound = 0, 256

        for i in range(0, (number_of_bytes_to_pad - 1)):
            random_number = lower_bound + secrets.randbelow(upper_bound)
            data_padded.append(random_number)  # random_hex

        data_padded.append(number_of_bytes_to_pad)  # last byte = number of padding bytes

        return data_padded
    """
    """

    # on hex strings
    def PKCS7 (self, data_hex_bytes_string, block_length):
        data_hex_bytes_string_padded = ''
        # to-do: check for proper hex string formats
        string_length = len(data_hex_bytes_string)

        while ((string_length % 2) != 0): # append zeros if the string_length is not even
            data_hex_bytes_string = '0' + data_hex_bytes_string
            string_length = string_length + 1

        byte_length = int(string_length/2)
        number_of_bytes_to_pad = block_length - byte_length # to-do, constrain to value 00 to FF

        if (number_of_bytes_to_pad != 0):
            value_to_pad = hex(number_of_bytes_to_pad).lstrip('0x')

            if (len(value_to_pad) != 2):
                value_to_pad = '0' + value_to_pad # append zero
        else:
            # value_to_pad = '00'
            value_to_pad = hex(block_length).lstrip('0x')

            if (len(value_to_pad) != 2):
                value_to_pad = '0' + value_to_pad # append zero

            number_of_bytes_to_pad = block_length # add another block when the block length is OK according to PKCS

        # start padding
        data_hex_bytes_string_padded = data_hex_bytes_string

        for i in range(0, number_of_bytes_to_pad):
            data_hex_bytes_string_padded = data_hex_bytes_string_padded + value_to_pad

        return data_hex_bytes_string_padded

    def zero_padding (self, data_hex_bytes_string, block_length): # Zero padding
        data_hex_bytes_string_padded = ''
        # to-do: check for proper hex string formats
        string_length = len(data_hex_bytes_string)

        while ((string_length % 2) != 0): # append zeros if the string_length is not even
            data_hex_bytes_string = '0' + data_hex_bytes_string
            string_length = string_length + 1

        byte_length = int(string_length/2)
        number_of_bytes_to_pad = block_length - byte_length # to-do, constrain to value 00 to FF

        """
        if (number_of_bytes_to_pad != 0):
            pass
        else:
            # value_to_pad = '00'
            number_of_bytes_to_pad = block_length # add another block when the block length is OK according to PKCS
        """
        # start padding
        data_hex_bytes_string_padded = data_hex_bytes_string

        for i in range(0, number_of_bytes_to_pad):
            data_hex_bytes_string_padded = data_hex_bytes_string_padded + '00'

        return data_hex_bytes_string_padded


    def OneAndZeroes (self, data_hex_bytes_string, block_length): # ISO/IEC 7816-4
        data_hex_bytes_string_padded = ''
        # to-do: check for proper hex string formats
        string_length = len(data_hex_bytes_string)

        while ((string_length % 2) != 0): # append zeros if the string_length is not even
            data_hex_bytes_string = '0' + data_hex_bytes_string
            string_length = string_length + 1

        byte_length = int(string_length/2)
        number_of_bytes_to_pad = block_length - byte_length # to-do, constrain to value 00 to FF

        if (number_of_bytes_to_pad != 0):
            pass
        else:
            # value_to_pad = '00'

            number_of_bytes_to_pad = block_length # add another block when the block length is OK according to PKCS

        # start padding
        data_hex_bytes_string_padded = data_hex_bytes_string

        # add 1st byte padding
        data_hex_bytes_string_padded = data_hex_bytes_string_padded + '80'

        for i in range(1, number_of_bytes_to_pad):
            data_hex_bytes_string_padded = data_hex_bytes_string_padded + '00'

        return data_hex_bytes_string_padded


    def ANSI_X9_23 (self, data_hex_bytes_string, block_length):
        data_hex_bytes_string_padded = ''
        # to-do: check for proper hex string formats
        string_length = len(data_hex_bytes_string)

        while ((string_length % 2) != 0): # append zeros if the string_length is not even
            data_hex_bytes_string = '0' + data_hex_bytes_string
            string_length = string_length + 1

        byte_length = int(string_length/2)
        number_of_bytes_to_pad = block_length - byte_length # to-do, constrain to value 00 to FF

        if (number_of_bytes_to_pad != 0):
            value_to_pad = hex(number_of_bytes_to_pad).lstrip('0x')

            if (len(value_to_pad) != 2):
                value_to_pad = '0' + value_to_pad # append zero
        else:
            # value_to_pad = '00'
            value_to_pad = hex(block_length).lstrip('0x')

            if (len(value_to_pad) != 2):
                value_to_pad = '0' + value_to_pad # append zero

            number_of_bytes_to_pad = block_length # add another block when the block length is OK according to PKCS

        # start padding
        data_hex_bytes_string_padded = data_hex_bytes_string

        for i in range(0, (number_of_bytes_to_pad-1)):
            data_hex_bytes_string_padded = data_hex_bytes_string_padded + '00'

        # add last byte value
        data_hex_bytes_string_padded = data_hex_bytes_string_padded + value_to_pad

        return data_hex_bytes_string_padded

    """
    def _ (self, data_hex_bytes_string, block_length):
        data_hex_bytes_string_padded = ''
        # ...
        return data_hex_bytes_string_padded
    """

    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = [];

        print("My name is Gaia [" + self.id + "].")

        return
    

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <padding_schemes>"
    print("=====[" + id + " Start]===== \n")
    padding_schemes_object = padding_schemes (id)
    padding_schemes_object.who_am_i()

    N = 8   # block_length; // Examples of PKCS5 padding for block length N = 8:
    data_hex_bytes_strings = ['FDFDFD', 'FDFDFDFDFDFDFD', 'FDFDFDFDFDFDFDFD']
    data_hex_bytes_strings_padded = []

    for i in range(0, len(data_hex_bytes_strings)):
        # data_hex_bytes_strings_padded.append(padding_schemes_object.PKCS7 (data_hex_bytes_strings[i], N))
        # data_hex_bytes_strings_padded.append(padding_schemes_object.ANSI_X9_23 (data_hex_bytes_strings[i], N))
        # data_hex_bytes_strings_padded.append(padding_schemes_object.OneAndZeroes (data_hex_bytes_strings[i], N))
        data_hex_bytes_strings_padded.append(padding_schemes_object.zero_padding(data_hex_bytes_strings[i], N))
        print(data_hex_bytes_strings_padded[i])

    """ PKCS5: 
    3 bytes: FDFDFD           --> FDFDFD0505050505
    7 bytes: FDFDFDFDFDFDFD   --> FDFDFDFDFDFDFD01
    8 bytes: FDFDFDFDFDFDFDFD --> FDFDFDFDFDFDFDFD0808080808080808
    """

    # import _Gaia._gaia
    # help(padding_schemes) # introspect


    print("=====[" + id + " End]===== \n");

"""
# version: 2018-04-04_1949hr_49sec
"""