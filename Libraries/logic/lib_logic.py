import os, sys
import numpy as np

# point to path
lib_path = os.path.abspath('../Libraries/data')
sys.path.append(lib_path)

from data_manipulator import data_manipulator 
from data_formatter import data_formatter

class lib_logic:
	""" Template model of Gaia """
	id = "lib_logic";
	inventory = {};
	inventory_id = "";
	
	operation_options = ['and', 'or', 'xor']
	operation_unary_options = ['not', 'shift_left', 'shift_right'] # to-do: 'rotate_left', 'rotate_right' 
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);

	def operation_between_2_binary_strings (self, binary_string_00, binary_string_01, operation_chosen):
		id_data_manipulator = "Library Function Agent: Internal Agent <data_manipulator>"
		print ("=====[" + id_data_manipulator + " Start]===== \n")
		data_manipulator_object = data_manipulator(id_data_manipulator)
		
		id_data_formatter = "Library Agent: Internal Agent <data_formatter>"
		print ("=====[" + id_data_formatter + " Start]===== \n")
		data_formatter_object = data_formatter(id_data_formatter)		
		# string to list type
		binary_string_00 = [binary_string_00]
		binary_string_01 = [binary_string_01]
		
		operation_unary_options = ['int_to_hex', 'hex_to_int', 'int_to_bin', 'bin_to_int', 'int_to_ascii', 'ascii_to_int', 'string_to_base64', 'base64_to_string']
		operation_chosen_data_format = operation_unary_options[3]
		
		value_int_00 = data_formatter_object.data_conversion_on_array(binary_string_00, operation_chosen_data_format)
		value_int_01 = data_formatter_object.data_conversion_on_array(binary_string_01, operation_chosen_data_format)
		
		# convert to int since it is just 1 item
		value_int_00 = value_int_00[0]
		value_int_01 = value_int_01[0]
		"""
		if (data_manipulator_object.array_or_matrix_dimensions_are_same(binary_string_00, binary_string_01)):
			print("binary strings: dimensions_are_same")
				
		else:
			print("array_or_matrix_dimensions_are_NOT_same")
			# make same length
			if (len(binary_string_00) > len(binary_string_01)):
				while (len(binary_string_00) > len(binary_string_01)):
					binary_string_01 = '0' + binary_string_01
			else:
				while (len(binary_string_00) < len(binary_string_01)):
					binary_string_00 = '0' + binary_string_00
		"""
		# start operation			
		if (operation_chosen == self.operation_options[0]):
			int_resultant = np.bitwise_and(value_int_00,value_int_01) 
		if (operation_chosen == self.operation_options[1]):
			int_resultant = np.bitwise_or(value_int_00,value_int_01) 
		if (operation_chosen == self.operation_options[2]):
			int_resultant = np.bitwise_xor(value_int_00,value_int_01)
		
		binary_resultant = bin(int_resultant)
		binary_resultant = binary_resultant.replace('0b', '')
		
		print ("=====[" + id_data_formatter + " End]===== \n")
		print ("=====[" + id_data_manipulator + " End]===== \n")
		
		return binary_resultant
		
	def operation_on_1_binary_string (self, binary_string_00, operation_chosen, number_of_times = 1):
		id_data_formatter = "Library Agent: Internal Agent <data_formatter>"
		print ("=====[" + id_data_formatter + " Start]===== \n")
		data_formatter_object = data_formatter(id_data_formatter)		
		# string to list type
		binary_string_00 = [binary_string_00]
		
		operation_unary_options = ['int_to_hex', 'hex_to_int', 'int_to_bin', 'bin_to_int', 'int_to_ascii', 'ascii_to_int', 'string_to_base64', 'base64_to_string']
		operation_chosen_data_format = operation_unary_options[3]
		
		value_int_00 = data_formatter_object.data_conversion_on_array(binary_string_00, operation_chosen_data_format)
		
		# convert to int since it is just 1 item
		value_int_00 = value_int_00[0]

		# start operation			
		if (operation_chosen == self.operation_unary_options[0]):
			# int_resultant = np.bitwise_not(value_int_00)
			int_resultant = np.invert(value_int_00) # NOT
		if (operation_chosen == self.operation_unary_options[1]):
			int_resultant = np.left_shift(value_int_00, number_of_times) 	
		if (operation_chosen == self.operation_unary_options[2]):
			int_resultant = np.right_shift(value_int_00, number_of_times) 
		
		binary_resultant = bin(int_resultant)
		binary_resultant = binary_resultant.replace('0b', '')
		print ("=====[" + id_data_formatter + " End]===== \n")
		
		return binary_resultant
				
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
	id_lib_logic = "Library Agent: Internal Agent <lib_logic>"
	print ("=====[" + id_lib_logic + " Start]===== \n")
	lib_logic_object = lib_logic(id_lib_logic)
	lib_logic_object.who_am_i()
	

	#import _Gaia._gaia
	#help(lib_logic) # introspect	
	
	print ("=====[" + id_lib_logic + " End]===== \n");
	
"""
# version: 2017-09-23_2010hr_04sec
"""		