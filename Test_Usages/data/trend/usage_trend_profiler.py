'''
data trend_profiler
'''
####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data/trend')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/display/console')
sys.path.append(lib_path)

# import package from path
from trend_profiler import trend_profiler	# file name
from data_generator import data_generator
from display_console import display_console	
from data_processor import data_processor

def generate_data_symbols (data_generator_object, number_of_data):
	upperBound = ord('z')
	lowerBound = ord('a')
	data = data_generator_object.generate_random_integers(number_of_data, upperBound, lowerBound)
	# map the numbers to symbols
	# ord('a') = 97
	# chr(97) = 'a'
	data_symbols = []
	
	for i in range(0, number_of_data):
		data_symbols.append(chr(data[i]))

	return data_symbols
	
def initialize_object (object_type, object_ID):
	id_object = "Test Usage Agent: <" + object_ID + ">"
	print ("=====[" + id_object + " Start]===== \n")
	object = object_type(id_object)
	
	return object
	
def declare_object_end (object_ID):
	print ("=====[" + object_ID + " End]=====")
	
	return None

####################################
## main
####################################
if __name__ == "__main__":
	display_console_object = initialize_object (display_console, 'display_console')
	data_generator_object = initialize_object (data_generator, 'data_generator')
	
	number_of_data = 20
	
	data_symbols = generate_data_symbols (data_generator_object, number_of_data)
	
	display_console_object.display_variable('data_symbols', data_symbols)
	
	data_processor_object = initialize_object (data_processor, 'data_processor')
	trend_profiler_object = initialize_object (trend_profiler, 'trend_profiler')
	
	symbol_to_hunt_for = 'a'
	
	display_console_object.display_variable('symbol_to_hunt_for', symbol_to_hunt_for)
	
	frequency_of_symbol = trend_profiler_object.find_frequency_of_symbol(data_symbols, symbol_to_hunt_for)
	display_console_object.display_variable('frequency_of_symbol', frequency_of_symbol)
	
	locations_of_symbol = trend_profiler_object.find_locations_of_symbol(data_symbols, symbol_to_hunt_for)
	display_console_object.display_variable('locations_of_symbol', locations_of_symbol)
	
	# given a list of symbols	
	symbol_list_to_hunt_for = ['a', 'g', 'h']
	display_console_object.display_variable('symbol_list_to_hunt_for', symbol_list_to_hunt_for)
	
	frequency_of_symbols = trend_profiler_object.find_frequency_of_symbol_list(data_symbols, symbol_list_to_hunt_for)
	display_console_object.display_variable('frequency_of_symbols', frequency_of_symbols)
	
	locations_of_symbols = trend_profiler_object.find_locations_of_symbol_list(data_symbols, symbol_list_to_hunt_for)
	display_console_object.display_variable('locations_of_symbols', locations_of_symbols)	
	
	unique_symbols = trend_profiler_object.get_unique_symbols(data_symbols)
	display_console_object.display_variable('unique_symbols', unique_symbols)	
	
	non_repeating_symbols = trend_profiler_object.get_non_repeating_symbols(data_symbols)
	display_console_object.display_variable('non_repeating_symbols', non_repeating_symbols)
	
	repeating_symbols = trend_profiler_object.get_repeating_symbols(data_symbols)
	display_console_object.display_variable('repeating_symbols', repeating_symbols)
	
	data_symbols_01 = generate_data_symbols (data_generator_object, number_of_data)
	
	display_console_object.display_variable('data_symbols_01', data_symbols_01)
	
	# get intersection 
	data_symbols_intersection = trend_profiler_object.get_intersection_symbols(data_symbols, data_symbols_01)
	
	display_console_object.display_variable('data_symbols_intersection', data_symbols_intersection)
	
	filter_values_list = ['a', 'e', 'i', 'o', 'u']
	filtered_data = data_processor_object.filter_values_given_filter_list (data_symbols_01, filter_values_list)
	
	display_console_object.display_variable('filtered_data', filtered_data)
	
	declare_object_end('data_processor')
	declare_object_end('trend_profiler')
	declare_object_end('data_generator')
	declare_object_end('display_console')
"""
# version: 2017-10-20_2214hr_16sec

"""