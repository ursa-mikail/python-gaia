import numpy as np

class lib_trigonometry:
	""" Template model of Gaia """
	id = "lib_trigonometry";
	inventory = {};
	inventory_id = "";
	
	operation_options = ['sine', 'cosine', 'tan', 'in_radians']
	operation_inverse_options = ['arc-sine', 'arc-cosine', 'arc-tan', 'in_degrees']
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);
		
	def operation_on_array_or_matrix (self, array_or_matrix, operation_chosen): # in radians. # Convert to radians by multiplying with pi/180 
		if (operation_chosen == self.operation_options[0]):
			martix_resultant = np.sin(array_or_matrix*np.pi/180) 
		if (operation_chosen == self.operation_options[1]):
			martix_resultant = np.cos(array_or_matrix*np.pi/180) 
		if (operation_chosen == self.operation_options[2]):
			martix_resultant = np.tan(array_or_matrix*np.pi/180) 
		if (operation_chosen == self.operation_options[3]):
			martix_resultant = (array_or_matrix*np.pi/180)
			
		return martix_resultant
		
	def operation_inverse_on_array_or_matrix (self, array_or_matrix, operation_chosen): # in degrees
	# Returned values are in radians. Apply np.degrees()
		if (operation_chosen == self.operation_inverse_options[0]):
			martix_resultant = np.degrees(np.arcsin(array_or_matrix))
		if (operation_chosen == self.operation_inverse_options[1]):
			martix_resultant = np.degrees(np.arccos(array_or_matrix))
		if (operation_chosen == self.operation_inverse_options[2]):
			martix_resultant = np.degrees(np.arctan(array_or_matrix))	
		if (operation_chosen == self.operation_inverse_options[3]):
			martix_resultant = np.degrees(array_or_matrix)			
			
		return martix_resultant		
				
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
	id = "Library Agent: Internal Agent <lib_trigonometry>"
	print ("=====[" + id + " Start]===== \n")
	lib_trigonometry_object = lib_trigonometry(id)
	lib_trigonometry_object.who_am_i()
	

	
	#import _Gaia._gaia
	#help(lib_trigonometry) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-09-23_2010hr_04sec
"""		