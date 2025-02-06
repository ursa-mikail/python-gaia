import numpy as np

import data_manipulator 

# data values are changed by this module
class data_processor:
	""" Template model of Gaia """
	id = "data_processor";
	inventory = {};
	inventory_id = "";
	
	operation_options = ['add', 'subtract', 'divide', 'multiply', 'remainder', 'power']
	operation_unary_options = ['reciprocal', 'floor', 'ceil', 'round', ]
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);

	# each element is applied to corresponding element on the 2nd matrix
	def arithmetic_operation_element_wise_between_2_arrays_or_matrices (self, array_or_matrix_00, array_or_matrix_01, operation_chosen):
		# id = "Library Function Agent: Internal Agent <data_manipulator>"
		# print ("=====[" + id + " Start]===== \n")
		# data_manipulator_object = data_manipulator.data_manipulator(id)
		
		# if (data_manipulator_object.array_or_matrix_dimensions_are_same(array_or_matrix_00, array_or_matrix_01)):
		if (len(np.array(array_or_matrix_00)) == len(np.array(array_or_matrix_01))):
			# print("array_or_matrix_dimensions_are_same")
			
			if (operation_chosen == self.operation_options[0]):
				martix_resultant = np.add(array_or_matrix_00,array_or_matrix_01) 
			if (operation_chosen == self.operation_options[1]):
				martix_resultant = np.subtract(array_or_matrix_00,array_or_matrix_01) 
			if (operation_chosen == self.operation_options[2]):
				martix_resultant = np.divide(array_or_matrix_00,array_or_matrix_01) 	
			if (operation_chosen == self.operation_options[3]):
				martix_resultant = np.multiply(array_or_matrix_00,array_or_matrix_01) 	
			if (operation_chosen == self.operation_options[4]):
				martix_resultant = np.mod(array_or_matrix_00,array_or_matrix_01) # np.remainder will give some results 	
			if (operation_chosen == self.operation_options[5]):
				martix_resultant = np.power(array_or_matrix_00,array_or_matrix_01) # raised to the power of the corresponding element in the 2nd input array.			
				
		else:
			print("array_or_matrix_dimensions_are_NOT_same")
			return None
		
		# print ("=====[" + id + " End]===== \n")
		
		return martix_resultant
		
	def arithmetic_operation_on_1_array_or_matrix (self, array_or_matrix, operation_chosen):
		if (operation_chosen == self.operation_unary_options[0]):
			martix_resultant = np.reciprocal(array_or_matrix) # numpy.reciprocal() returns the reciprocal of argument, element-wise. For elements with absolute values > 1, the result is always 0 because of the way in which Python handles integer division. For integer 0, an overflow warning is issued.	
		if (operation_chosen == self.operation_unary_options[1]):
			martix_resultant = np.floor(array_or_matrix)
		if (operation_chosen == self.operation_unary_options[2]):
			martix_resultant = np.ceil(array_or_matrix)
		if (operation_chosen == self.operation_unary_options[3]):
			martix_resultant = np.round(array_or_matrix)
			
		return martix_resultant
		
	def filter_values_given_filter_list (self, data, filter_values_list): 
		filtered_data = []
		flag_value_not_found = True
		
		for data_index in range(0, len(data)):
			for symbols_to_filter_list_index in range(0, len(filter_values_list)):
				if (data[data_index] == filter_values_list[symbols_to_filter_list_index]): # HIT, therefore skip the data (not record) and filter
					flag_value_not_found = False
					
					continue # halt the search and go to the next data
			# determine to record the data or not		
			if (flag_value_not_found == True):		
				filtered_data.append(data[data_index])
			else:	# reset it and not record the data
				flag_value_not_found = True
					
		return filtered_data
		
	# mapping_table_list is a dictionary	
	def translate_data_with_mapping_list(self, data, mapping_table_list): 
		translated_data = []
		
		dictionary_key_list = list(mapping_table_list.keys())
		dictionary_value_list = list(mapping_table_list.values())
		length_of_dictionary = len(dictionary_key_list)
		
		for data_index in range(0, len(data)):
			for mapping_list_index in range(0, length_of_dictionary):
				if (data[data_index] == dictionary_key_list[mapping_list_index]): # this assumes the symbol is not exclusive of the mapping_table_list, i.e. it must be found on the mapping table
					translated_data.append(dictionary_value_list[mapping_list_index])
		
		return translated_data
				
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
	id = "Library Agent: Internal Agent <data_processor>"
	print ("=====[" + id + " Start]===== \n")
	data_processor_object = data_processor(id)
	data_processor_object.who_am_i()
	

	
	#import _Gaia._gaia
	#help(data_processor) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-09-23_2010hr_04sec
"""		