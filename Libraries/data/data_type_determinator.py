import numpy as np

####################################
# int_type : c data type (4 byte size)
class int_type:
	number_of_bytes = 4;
	number_of_bits_in_1_byte = 8;
	
	def generate_value_range(self):
		for x in xrange(0, 2**(self.number_of_bytes * self.number_of_bits_in_1_byte)):
			value = x;
			print ("\n", x)
			
	def get_data_range(self):
		self.max= (2**(self.number_of_bytes * self.number_of_bits_in_1_byte)/2) - 1;
		self.min = - (2**(self.number_of_bytes * self.number_of_bits_in_1_byte)/2);		
		print ("Upper bound = ", self.max, "\n")
		print ("Lower bound = ", self.min, "\n")

# signed_type : c data type (4 byte size)
class signed_type(int_type):
	pass;
	
# unsigned_int_type : c data type (4 byte size)
class unsigned_int_type(int_type):

	def get_data_range(self):
		self.max= (2**(self.number_of_bytes * self.number_of_bits_in_1_byte)) - 1;
		self.min = 0;		
		print ("Upper bound = ", self.max, "\n")
		print ("Lower bound = ", self.min, "\n")	
		
# unsigned_type : c data type (4 byte size)
class unsigned_type(unsigned_int_type):		
	pass;
	
# _int8_type : c data type (1 byte size)
class _int8_type(int_type):
	number_of_bytes = 1;

# char_type : c data type (1 byte size)
class char_type(_int8_type):
	pass; # Caveat: In some systems, it is 0 to 255, while in other, it is -128 to 127  by default
	
# unsigned_int8_type : c data type (1 byte size)
class unsigned_int8_type(unsigned_int_type):
	number_of_bytes = 1;

# unsigned_char_type : c data type (1 byte size)
class unsigned_char_type(unsigned_int8_type):
	pass; 	
	
# signed_char_type : c data type (1 byte size)
class signed_char_type(_int8_type):
	pass; 	
	
# _int16_type : c data type (2 byte size)
class _int16_type(int_type):
	number_of_bytes = 2;
	
# short_type : c data type (2 byte size)
class short_type(_int16_type):
	pass;
	
# short_int_type : c data type (2 byte size)
class short_int_type(_int16_type):
	pass;
	
# signed_short_int_type : c data type (2 byte size)
class signed_short_int_type(_int16_type):
	pass;
	
# unsigned_int16_type : c data type (2 byte size)
class unsigned_int16_type(unsigned_int_type):
	number_of_bytes = 2;
	
# unsigned_short_type : c data type (2 byte size)
class unsigned_short_type (unsigned_int16_type):
	pass;
	
# unsigned_short_int_type : c data type (2 byte size)
class unsigned_short_int_type (unsigned_int16_type):
	pass;	

# _int32_type : c data type (4 byte size)
class _int32_type(int_type):
	pass;
	
# signed_int_type : c data type (4 byte size)
class signed_int_type(_int32_type):
	pass;

# _int64_type : c data type (8 byte size)
class _int64_type(int_type):
	number_of_bytes = 8;	

# long_long_type : c data type (4 byte size)
class long_long_type(_int64_type):
	pass;	
	
# signed_long_long_type : c data type (4 byte size)
class signed_long_long_type(_int64_type):
	pass;	
	
# unsigned_int64_type : c data type (8 byte size)
class unsigned_int64_type(unsigned_int_type):
	number_of_bytes = 8;	
	
# unsigned_long_long_type : c data type (8 byte size)
class unsigned_long_long_type(unsigned_int64_type):
	pass;		
	

# bool_type : c data type (0 byte size, 1 bit size)
class bool_type(unsigned_int64_type):
	number_of_bytes = 0;		
	
	def get_data_range(self):
		self.max= 1;
		self.min = 0;		
		print ("Upper bound = ", self.max, "\n")
		print ("Lower bound = ", self.min, "\n")		
	
# long_type : c data type (4 byte size)
class long_type(int_type):
	number_of_bytes = 4;
	
# long_int_type : c data type (4 byte size)
class long_int_type(long_type):
	pass;
	
# signed_long_int_type : c data type (4 byte size)
class signed_long_int_type(long_type):
	pass;	
	
# unsigned_long_type : c data type (4 byte size)
class unsigned_long_type(unsigned_int_type):
	number_of_bytes = 4;
	
# unsigned_long_int_type : c data type (4 byte size)
class unsigned_long_int_type(unsigned_long_type):
	pass;

# wchar_t_type : c data type (2 byte size)
class wchar_t_type(unsigned_short_type):
	pass;
	
class data_form_determinator ():
	id = "data_form_determinator";
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);
		
	# return array or element, and length	
	def is_array_or_element(self, data_target):
		if (np.isscalar(data_target)):
			length = 1
			data_form = 'element'
		else:
			length = len(data_target)
			data_form = 'array'
		
		return data_form, length
	
	def who_am_i(self): # 
		""" Introspection """
		self.line_storage = [];
		
		print ("My name is Gaia [" + self.id + "].")
		
		return
		
	def __del__(self):
		print ("_gaia object [%s] removed\n" % self.id);
	
# Ref: http://msdn.microsoft.com/en-us/library/s3f49ktz.aspx	
# `enum`, `float`, `double` (same as long double) yet to be defined	

# float := 1 bit sign; 11 bits exponent; 52 bits fraction

# (-1)*bit_sign
# 1 + sum(bits_fraction); sum(bits_exponent) := sum(b_(52-i)*(2**-i)), i := 1:52
# 2** (int(bits_fraction, 2) - 1023)
# Ref:
#		http://en.wikipedia.org/wiki/Double-precision_floating-point_format
#		http://stackoverflow.com/questions/10108053/ranges-of-floating-point-datatype-in-c

"""	
####################################
## main
####################################
if __name__ == "__main__":
	print "Getting range value for int type.";
	int_object = int_type();
	#int_object.generate_value_range();
	int_object.get_data_range();
	
	print "Getting range value for unsigned int type.";
	unsigned_int_object = unsigned_int_type();
	unsigned_int_object.get_data_range();
	
	print "Getting range value for _int8 type.";
	_int8_object = _int8_type();
	_int8_object.get_data_range();
	
	print "Getting range value for char type.";
	char_object = char_type();
	char_object.get_data_range();
	
	print "Getting range value for unsigned_int8 type.";
	unsigned_int8_object = unsigned_int8_type();
	unsigned_int8_object.get_data_range();
	
	print "Getting range value for _int16 type.";
	_int16_object = _int16_type();
	_int16_object.get_data_range();
	
	print "Getting range value for signed_long_long type.";
	signed_long_long_object = signed_long_long_type();
	signed_long_long_object.get_data_range();
	
	print "Getting range value for unsigned_int64 type.";
	unsigned_int64_object = unsigned_int64_type();
	unsigned_int64_object.get_data_range();
	
	print "Getting range value for bool type.";
	bool_object = bool_type();
	bool_object.get_data_range();
"""












