## usage_generate_data: usage_ has to be appended for this file to avert confuse of initializing with this file instead of correctly with the import one
####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/cryptography/data_generation')
sys.path.append(lib_path)

# import package from path
import generator_data	# file name

####################################
## main
####################################

numberOfRandomStrings = 2; lengthOfDigits = 25; upperBound = 255; lowerBound = 0;
data_generator_object = generator_data.generator_data();
data_generator_object.generate_random_value(numberOfRandomStrings, lengthOfDigits, upperBound, lowerBound);
print ("Printing value for int type.")
data_generator_object.print_matrix_int();
row_size = len(data_generator_object.randomValueCandidate_matrix);
column_size = len(data_generator_object.randomValueCandidate_matrix[0]);
print (row_size, ",", column_size)
matrix_hex = data_generator_object.matrix_to_hex(data_generator_object.randomValueCandidate_matrix, row_size, column_size);
data_generator_object.print_matrix(matrix_hex, row_size, column_size);

data_generator_object.__del__();
print ("\n")

# generate random shuffled indices
rangeOfIndices = 15;  # 0:rangeOfIndices
data_generator_object = generator_data.generator_data();
data_generator_object.generate_random_indices(rangeOfIndices)

'''
There will be double printing as there is also a main in that local package as a local unit test
'''