'''
Demonstrating the Utility of Gaia 
'''
####################################
import os, sys

# point to path
lib_path = os.path.abspath('../Libraries/Lib_00')
sys.path.append(lib_path)

# import package from path
import _lib;	# file name

####################################
## main
####################################
if __name__ == "__main__":
	id = "Utility Agent"
	print ("=====[" + id + " Start]===== \n");
	_gaia_object = _lib._lib_class(id); # file_name.class_name
	number_of_lines = _gaia_object.who_am_i();

	print ("=====[" + id + " End]===== \n");

