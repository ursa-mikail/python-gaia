####################################
import os, sys
import string
import math

# point to path
lib_path = os.path.abspath('../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from data_generator import data_generator	# file name

def list_subtraction (list1, list2):
	list_resultant = []
	for i in range(0, len(list1)):
		list_resultant.append(list1[i] - list2[i])
		
	return list_resultant
	

####################################
## main
####################################
if __name__ == "__main__":
	id_data_generator = "Test Usage Agent: <data_generator>" 
	print ("=====[" + id_data_generator + " Start]===== \n")
	data_generator_object = data_generator(id_data_generator)
	data_generator_object.who_am_i()
	number_of_points = 10
	mu, sigma = 0, 0.1 # mean and standard deviation
	mu, sigma = 0, 1 # mean and standard deviation
	data_points = data_generator_object.generate_data_given_mean_and_variance (mu, sigma, number_of_points) 
	print(data_points)
	"""
	standard_deviation = np.std(data_points, dtype=np.float64)
	mean = np.mean(data_points, dtype=np.float64)
	print("standard_deviation:" + str(standard_deviation))
	print("mean:" + str(mean))
	"""
	numberOfRandomStrings = 2; lengthOfDigits = 5; #1
	upperBound = 9; lowerBound = 0;
	# data_points = data_generator_object.generate_random_integers (lengthOfDigits, upperBound, lowerBound) 
	data_points = data_generator_object.generate_random_floats(lengthOfDigits, upperBound, lowerBound) 
	print(data_points)
	
	number_of_bytes = 5
	random_bytes_string = data_generator_object.generate_random_bytes_string(number_of_bytes)
	print(random_bytes_string)	
	
	length_of_indices = 7
	indices_shuffled = data_generator_object.generate_scrambled_indices (length_of_indices)
	print(indices_shuffled)
	
	# generate data and hunt for the mean 
	# scenario 1
	mu, sigma = 0, 100 # mean and standard deviation
	# number_of_points = 5000000
	number_of_points = 50
	data_points = data_generator_object.generate_data_given_mean_and_variance (mu, sigma, number_of_points) 
	print(data_points)
	print('max: ', max(data_points))
	print('min: ', min(data_points))
	print('estimated mean: ', sum(data_points)/number_of_points)
	
	# scenario 2
	number_of_data_points, upperBound, lowerBound = 100000, 100, 10
	constant_true = 5
	data_points = data_generator_object.generate_random_integers (number_of_data_points, upperBound, lowerBound)
	data_points = list_subtraction(data_points,([constant_true]*number_of_data_points))
	
	print(data_points)
	mid_point = (max(data_points) - min(data_points))/2
	print('max: ', max(data_points))
	print('min: ', min(data_points))
	print('mid: ', mid_point)
	
	normalized_data_points = list_subtraction(data_points,([mid_point]*number_of_data_points))
	# print(normalized_data_points)
	
	print('estimated mean: ', sum(normalized_data_points)/number_of_data_points)

	for i in range(0, 10):
		upper_range, lower_range = 10, 0
		r1 = data_generator_object.generate_random_float(upper_range, lower_range)
		print("Random number between 0 and 10 is %s" % (r1))

	# symbol_list = ['wa', '4', 're', '1%0', 'angel']
	# symbol_list = string.ascii_letters
	symbol_list = string.ascii_letters[0:6]
	symbol_list = symbol_list + '0123456789'

	for i in range(0, 10):
		r1 = data_generator_object.generate_random_symbols(symbol_list)
		print("Chosen is %s " % (r1), "from list: %s" % (symbol_list))

	data_generator_object.generate_random_time_in_day()
	
	print ("=====[" + id_data_generator + " End]===== \n");
	
"""
# version: 2017-09-23_2010hr_04sec
"""	