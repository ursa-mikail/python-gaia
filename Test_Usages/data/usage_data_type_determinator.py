import os, sys
import numpy as np

# point to path
lib_path = os.path.abspath('../../Libraries/data')
sys.path.append(lib_path)

# import package from path
import data_type_determinator
from data_type_determinator	import data_form_determinator

# import /data_generation/data_generation.py;

####################################
	
####################################
## main
####################################
if __name__ == "__main__":
	print ("""
*********************************************** 
		[START] 
***********************************************
	""")
	print ("Getting range value for int type.")
	int_object = data_type_determinator.int_type();
	#int_object.generate_value_range();
	int_object.get_data_range();
	
	print ("Getting range value for unsigned int type.")
	unsigned_int_object = data_type_determinator.unsigned_int_type();
	unsigned_int_object.get_data_range();
	
	print ("Getting range value for _int8 type.")
	_int8_object = data_type_determinator._int8_type();
	_int8_object.get_data_range();
	
	print ("Getting range value for char type.")
	char_object = data_type_determinator.char_type();
	char_object.get_data_range();
	
	print ("Getting range value for unsigned_int8 type.")
	unsigned_int8_object = data_type_determinator.unsigned_int8_type();
	unsigned_int8_object.get_data_range();
	
	print ("Getting range value for _int16 type.")
	_int16_object = data_type_determinator._int16_type();
	_int16_object.get_data_range();
	
	print ("Getting range value for signed_long_long type.")
	signed_long_long_object = data_type_determinator.signed_long_long_type();
	signed_long_long_object.get_data_range();
	
	print ("Getting range value for unsigned_int64 type.")
	unsigned_int64_object = data_type_determinator.unsigned_int64_type();
	unsigned_int64_object.get_data_range();
	
	print ("Getting range value for bool type.")
	bool_object = data_type_determinator.bool_type();
	bool_object.get_data_range();
	
	
	print (np.isscalar(3.1)) # True
	print (np.isscalar([3.1])) # False
	print (np.isscalar("string")) # True

	id_data_form_determinator = "Library Agent: Internal Agent <data_form_determinator>"
	print ("=====[" + id_data_form_determinator + " Start]===== \n")
	data_form_determinator_object = data_form_determinator(id)
	
	list_of_data = [3.1, [3.1], "string", [0, 1, "string_00", 55, None]]
	number_of_items = len(list_of_data)
	
	for i in range(0, number_of_items):
		data_form, length = data_form_determinator_object.is_array_or_element(list_of_data[i])
		print ("item: ", list_of_data[i], "\t", "data_form: ", data_form, "\t", "length: ", length)
	
	
	#import _Gaia._gaia
	#help(data_form_determinator) # introspect	
	
	print ("=====[" + id_data_form_determinator + " End]===== \n");	
	
	print ("""
*********************************************** 
		[END] 
***********************************************
	""")
	











