import binascii
import base64
import codecs

# 
class data_formatter:
    """ Template model of Gaia """
    id = "data_formatter"
    inventory = {}
    inventory_id = ""

    operation_unary_options = ['int_to_hex', 'hex_to_int', 'int_to_bin', 'bin_to_int',
                               'int_to_ascii', 'ascii_to_int', 'string_to_base64', 'base64_to_string',
                               'hex_to_base64', 'base64_to_hex', 'hex_bytes_list_to_hex_string']

    operation_python_data_string_to_and_from_byte_object_options = ['string_to_bytes_object', 'bytes_object_to_string',
                                                                    'ascii_string_to_hex_string', 'hex_string_to_ascii_string',
                                                                    'ascii_bytes_object_to_hex_bytes_object', 'hex_bytes_object_to_ascii_bytes_object',
                                                                    'int_array_to_byte_array', 'byte_array_object_to_string',
                                                                    'string_to_byte_array', 'byte_array_to_int_array'] # 'byte_array' := binary object

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id);

    def data_conversion_on_array (self, array_target, operation_chosen):
        array_resultant = []

        if (operation_chosen == self.operation_unary_options[0]):
            for i in range(0, len(array_target)):
                hex_string = hex(array_target[i]).lstrip("0x")
                if (len(hex_string) == 0):
                    hex_string = '0'

                array_resultant.append(hex_string)
        if (operation_chosen == self.operation_unary_options[1]):
            for i in range(0, len(array_target)):
                value_int = int(array_target[i], 16)
                array_resultant.append(value_int)

        if (operation_chosen == self.operation_unary_options[2]):
            for i in range(0, len(array_target)):
                value_binary = bin(array_target[i]).lstrip('0b')
                if (len(value_binary) == 0):
                    value_binary = '0'
                array_resultant.append(value_binary)

        if (operation_chosen == self.operation_unary_options[3]):
            for i in range(0, len(array_target)):
                value_int = int(array_target[i], 2)
                array_resultant.append(value_int)

        if (operation_chosen == self.operation_unary_options[4]):
            # array_resultant = ["" for x in range(len(array_target))] # allocate memory for string array
            for i in range(0, len(array_target)):
                if ((array_target[i] >= 0) & (array_target[i] < 256)):
                    string_ascii = chr(array_target[i])
                else:
                    string_ascii = 'exceed_range'

                if (string_ascii != 'exceed_range'):
                    array_resultant.append(string_ascii)

        if (operation_chosen == self.operation_unary_options[5]):
            for i in range(0, len(array_target)):
                value_int = ord(array_target[i])
                array_resultant.append(value_int)
        if (operation_chosen == self.operation_unary_options[6]):
            for i in range(0, len(array_target)):
                value_base64 = str(base64.b64encode(bytes(array_target[i], 'utf-8'))).lstrip("b'").rstrip("'")
                array_resultant.append(value_base64)

        if (operation_chosen == self.operation_unary_options[7]):
            for i in range(0, len(array_target)):
                string_buffer = str(base64.b64decode(array_target[i])).lstrip("b'").rstrip("'")
                array_resultant.append(string_buffer)

        if (operation_chosen == self.operation_unary_options[8]):
            for i in range(0, len(array_target)):
                string_buffer = codecs.encode(codecs.decode(array_target[i].encode('ascii'), 'hex'), 'base64')
                string_buffer = string_buffer.decode('ascii').rstrip("\n")
                string_buffer = string_buffer.replace("\n", "")
                array_resultant.append(string_buffer)

        if (operation_chosen == self.operation_unary_options[9]):
            for i in range(0, len(array_target)):
                array_target[i] = array_target[i].encode('ascii')
                string_buffer = codecs.encode(codecs.decode(array_target[i], 'base64'), 'hex')
                string_buffer = string_buffer.decode('ascii')
                array_resultant.append(string_buffer)

        if (operation_chosen == self.operation_unary_options[10]):
            array_resultant = ""
            for i in range(0, len(array_target)):
                if ((len(array_target[i])%2) != 0): # if not even character in the array buffer
                    array_resultant = array_resultant + '0' + array_target[i]
                else:
                    array_resultant = array_resultant + array_target[i]

        return array_resultant
    """
    byte object -> decode('ascii') -> string -> encode('ascii') -> byte object
    """
    def data_conversion_hex_and_bytes_object (self, data, operation_chosen):
        resultant = None

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[0]):
            resultant = data.encode('ascii')   # ascii string to bytes ascii object
            """
            # To convert a string to bytes.
            data_string = "test"  			#string
            data_bytes = data_string.encode()	#bytes
            # data_bytes = b"test" 			#bytes
            print (data_bytes)
            print (data_bytes[0]) # in decimal value
            """

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[1]):
            resultant = data.decode('ascii')  # bytes ascii object to ascii string
            """
            # To convert bytes to a string.
            data_bytes = b"test"  		#bytes
            data_string = data_bytes.decode() #string
            #data_string = str(b"test")  	#string
            print (data_string)
            """
        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[2]):
            data = data.encode('ascii') # to bytes object
            data = codecs.encode(data, 'hex') # ascii_string_to_hex_string
            resultant = data.decode('ascii') # to string

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[3]):
            data = data.encode('ascii')  # to bytes object
            data = codecs.decode(data, 'hex')  # hex_string_to_ascii_string
            resultant = data.decode('ascii')  # to string

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[4]):
            resultant = codecs.encode(data, 'hex')  # ascii_bytes_to_hex_bytes

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[5]):
            resultant = codecs.decode(data, 'hex') # hex_bytes_to_ascii_bytes

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[6]):
            resultant = bytearray(data)  # int array to byte array

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[7]):
            resultant = data.decode("utf-8") # byte array to string, e.g. b"abcde".decode("utf-8")

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[8]):
            resultant = data.encode("utf-8") # string to byte array, e.g.

        if (operation_chosen == self.operation_python_data_string_to_and_from_byte_object_options[9]):
            resultant = []
            for i in range(0, len(data)):
                resultant.append(data[i])

        return resultant

    def who_am_i(self): #
        """ Introspection """
        self.line_storage = [];

        print ("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print ("_gaia object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <data_formatter>"
    print ("=====[" + id + " Start]===== \n")
    data_formatter_object = data_formatter(id)
    data_formatter_object.who_am_i()



    #import _Gaia._gaia
    #help(data_formatter) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2018-01-08_1701hr_59sec
"""		