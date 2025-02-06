import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/logic')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from data_manipulator import data_manipulator 
from lib_logic import lib_logic 
from data_formatter import data_formatter


####################################
operation_unary_options_data_format = ['int_to_hex', 'hex_to_int', 'int_to_bin', 'bin_to_int', 'int_to_ascii', 'ascii_to_int', 'string_to_base64', 'base64_to_string']

operation_options_logic = ['and', 'or', 'xor']
operation_unary_options_logic = ['not', 'shift_left', 'shift_right'] # to-do: 'rotate_left', 'rotate_right'
	
	
####################################
## main
####################################
if __name__ == "__main__":
	id = "Usage Agent: <lib_logic>"
	print ("=====[" + id + " Start]===== \n")
	lib_logic_object = lib_logic(id)
	lib_logic_object.who_am_i()
	value_int_00, value_int_01 = [103], [1007] # single lists of integer
	
	id_data_formatter = "Usage Agent: <data_formatter>"
	print ("=====[" + id_data_formatter + " Start]===== \n")
	data_formatter_object = data_formatter(id_data_formatter)
	
	operation_chosen = operation_unary_options_data_format[2]
	
	value_binary_00 = data_formatter_object.data_conversion_on_array(value_int_00, operation_chosen)
	value_binary_01 = data_formatter_object.data_conversion_on_array(value_int_01, operation_chosen)
	# convert to string since it is just 1 item
	value_binary_00 = value_binary_00[0]
	value_binary_01 = value_binary_01[0]
	
	id_lib_logic = "Library Agent: Internal Agent <lib_logic>"
	print ("=====[" + id_lib_logic + " Start]===== \n")
	lib_logic_object = lib_logic(id_lib_logic)
	
	print (value_binary_00)
	print (value_binary_01)
	
	operation_chosen = operation_options_logic[0]
	operation_chosen = operation_options_logic[2]
	
	binary_resultant = lib_logic_object.operation_between_2_binary_strings ( value_binary_00, value_binary_01, operation_chosen)
	print(binary_resultant)
	
	operation_chosen = operation_unary_options_logic[0]
	binary_resultant = lib_logic_object.operation_on_1_binary_string ( value_binary_00, operation_chosen)
	print(binary_resultant)
	
	operation_chosen = operation_unary_options_logic[1]
	number_of_times = 50
	binary_resultant = lib_logic_object.operation_on_1_binary_string ( value_binary_00, operation_chosen, number_of_times)
	print(binary_resultant)	
	
	operation_chosen = operation_unary_options_logic[2]
	number_of_times = 50
	binary_resultant = lib_logic_object.operation_on_1_binary_string ( value_binary_00, operation_chosen, number_of_times)
	print(binary_resultant)	
	
	#import _Gaia._gaia
	#help(lib_logic) # introspect
	
	print ("=====[" + id_lib_logic + " End]===== \n")
	print ("=====[" + id_data_formatter + " End]===== \n")
		
	#import _Gaia._gaia
	#help(lib_logic) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
	











