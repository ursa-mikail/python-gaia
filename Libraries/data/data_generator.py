import numpy as np,numpy.random
from random import randint
from random import *
import random
import math


import os
import base64

class data_generator:
	""" Template model of Gaia """
	id = "";
	inventory = {};
	inventory_id = "";
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id)

	def generate_random_int(self, upper_range, lower_range):
		assert (upper_range >= lower_range)
		r1 = random.randint(lower_range, upper_range)

		return r1

	def generate_random_float(self, upper_range, lower_range):
		assert (upper_range >= lower_range)
		r1 = random.uniform(lower_range, upper_range)

		return r1

	def generate_random_symbols(self, symbol_list):
		# index_chosen = self.generate_random_int(len(symbol_list)-1 , 0)
		# r1 = symbol_list[index_chosen]

		r1 = random.choice(symbol_list)  # (string.ascii_letters)

		return r1

	def generate_random_time_in_day_in_secs(self):
		upper_range, lower_range = (24 * 60 * 60) - 1, 0
		t = self.generate_random_int(upper_range, lower_range)

		return t

	def generate_random_time_in_day(self):
		t = self.generate_random_time_in_day_in_secs()
		upper_range, lower_range = (24 * 60 * 60) - 1, 0
		print('Random number between', upper_range, ' and ', lower_range, ' is ', t)
		# t = upper_range
		hr = math.floor(t / (60 * 60))

		t = t - (hr * 60 * 60)
		mins = math.floor(t / 60)
		t = t - (mins * 60)
		secs = t

		print(hr, ":", mins, ":", secs)

		return t

	def generate_data_given_mean_and_variance(self, mean, variance, number_of_data_points): # 
		data_points = np.random.normal(mean, variance, number_of_data_points)
		
		return data_points
		
	def generate_random_integers(self, number_of_data_points, upperBound, lowerBound):
		data_points = []
		
		if (number_of_data_points == 1):
			return randint(lowerBound, upperBound)
		
		for x in range(0, number_of_data_points): 
			randomValueCandidate = randint(lowerBound, upperBound) #Inclusive
			data_points.append(randomValueCandidate)
			
		return data_points
		
	def generate_random_floats(self, number_of_data_points, upperBound, lowerBound):
		data_points = []
		
		if (number_of_data_points == 1):
			return uniform(lowerBound, upperBound)
		
		for x in range(0, number_of_data_points): 
			randomValueCandidate = uniform(lowerBound, upperBound) #Inclusive
			data_points.append(randomValueCandidate)
			
		return data_points	

	def generate_random_bytes_string(self, number_of_bytes):
		random_bytes = os.urandom(number_of_bytes)
		random_bytes_string = "";
		
		for i in range(0, len(random_bytes)):
			random_byte_candidate = str(hex(random_bytes[i])).lstrip('0x')
			
			if (len(random_byte_candidate) == 1): # append a '0'
				random_byte_candidate = '0' + random_byte_candidate
			
			# print(random_byte_candidate)
			random_bytes_string = random_bytes_string + random_byte_candidate # + " "

		random_bytes_string = str(random_bytes_string);
		
		
		""" base65 conversion
		random_bytes_string = base64.b64encode(random_bytes)   # in base64
		random_bytes_string = str(random_bytes_string)
		random_bytes_string = random_bytes_string.lstrip("b'").rstrip("'")
		"""
		return random_bytes_string		
		
	def generate_scrambled_indices(self, size):
		#alphabet_indices_original = []
		indices_scrambled = []
		
		for i in range(0, size):
			indices_scrambled.append(i);
			#alphabet_indices_original.append(i+1);

		shuffle(indices_scrambled)
		#print indices_scrambled;
		#print alphabet_indices_original;

		return indices_scrambled		
				
	def who_am_i(self): # read from file
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
	id = "Library Agent: Internal Agent <data_generator>"
	print ("=====[" + id + " Start]===== \n")
	data_generator_object = data_generator(id)
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
	
	#import _Gaia._gaia
	#help(data_generator) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-09-23_2010hr_04sec
"""		