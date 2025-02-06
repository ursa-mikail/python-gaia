####################################
import os, sys
import numpy as np


# point to path
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/math/trigonometry')
sys.path.append(lib_path)

# import package from path
from data_processor import data_processor	# file name
from data_manipulator import data_manipulator
from lib_trigonometry import lib_trigonometry	

####################################
## main
####################################
if __name__ == "__main__":
	id_data_processor = "Library Agent: Internal Agent <data_processor>"
	id_data_manipulator = "Library Agent: Internal Agent <data_manipulator>"	
	id_lib_trigonometry = "Library Agent: Internal Agent <lib_trigonometry>"	
	
	print ("=====[" + id_data_processor + " Start]===== \n")
	print ("=====[" + id_data_manipulator + " Start]===== \n")	
	print ("=====[" + id_lib_trigonometry + " Start]===== \n")
	
	data_processor_object = data_processor(id_data_processor)
	data_manipulator_object = data_manipulator(id_data_manipulator)	
	lib_trigonometry_object  = lib_trigonometry(id_lib_trigonometry)
	
	#zeroized_flag = False
	#N, M, data_type = 5, 8, 'float' # 'int'
	#matrix_NxM_00 = data_manipulator_object.create_matrix_NxM (N, M, data_type, zeroized_flag)
	
	data_type = 'float'
	list_of_values = [0,30,45,60,90]
	matrix_NxM_00 = data_manipulator_object.create_list_to_array (data_type, list_of_values)
	
	print("matrix_NxM_00:\n" + str(matrix_NxM_00))
	
	# axis-0: row-wise; axis-1: column-wise; 
	operation_options = ['sine', 'cosine', 'tan', 'in_radians']
	action_chosen = operation_options[len(operation_options)-1]
	
	martix_resultant = lib_trigonometry_object.operation_on_array_or_matrix(matrix_NxM_00, action_chosen)
	print("Operation: " + action_chosen)
	print(martix_resultant)
	
	operation_inverse_options = ['arc-sine', 'arc-cosine', 'arc-tan', 'in_degrees']
	action_chosen = operation_inverse_options[len(operation_inverse_options)-1]
	
	martix_resultant_00 = lib_trigonometry_object.operation_inverse_on_array_or_matrix(martix_resultant, action_chosen)
	print("Operation: " + action_chosen)
	print(martix_resultant_00)

	print ("=====[" + id_lib_trigonometry + " End]===== \n");	
	print ("=====[" + id_data_manipulator + " End]===== \n");
	print ("=====[" + id_data_processor + " End]===== \n");
"""
# version: 2017-09-23_2010hr_04sec
"""	