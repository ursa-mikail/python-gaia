## generator_data
####################################
from random import randint
import array

# _
class generator_data:
# generate_int_type:
	# randomValueCandidate_matrix[][];

	def init_matrix(self, numberOfRandomStrings, lengthOfDigits):
		# Creates a list containing  numberOfRandomStrings` lists initialized to 0
		self.row_size = numberOfRandomStrings;
		self.column_size = lengthOfDigits;		
		self.randomValueCandidate_matrix = [[0 for x in range(self.column_size)] for x in range(self.row_size)] 
		self.matrix_hex = [[0 for x in range(self.column_size)] for x in range(self.row_size)] 
		
	def generate_random_value(self, numberOfRandomStrings, lengthOfDigits, upperBound, lowerBound):
		# Creates a list containing  numberOfRandomStrings` lists initialized to 0
		self.init_matrix(numberOfRandomStrings, lengthOfDigits);
		#randomValueCandidate_matrix = [[0 for x in range(column_size)] for x in range(row_size)] 
	
		for x in range(1, (numberOfRandomStrings+1)):   # N random strings
			for y in range(1, (lengthOfDigits+1)):  # each M digits
				randomValueCandidate = randint(lowerBound, upperBound) #Inclusive
				self.randomValueCandidate_matrix[x-1][y-1] = randomValueCandidate;
				#print ("%d" % randomValueCandidate),
				#print ("%d" % self.randomValueCandidate_matrix[x-1][y-1]), # print without newline
			#print "\n"
			
	def print_matrix_int(self):
		for x in range(1, (self.row_size+1)):   # N random strings
			for y in range(1, (self.column_size+1)):  # each M digits
				print ("%d" % self.randomValueCandidate_matrix[x-1][y-1]), # print without newline
			print ("\n")
			
	def print_matrix(self, matrix_buffer, row_size, column_size):
		for x in range(1, (row_size+1)):   # N strings
			for y in range(1, (column_size+1)):  # each M digits
				print ("%s" % matrix_buffer[x-1][y-1]), # print without newline
			print ("\n")			
	
	# uses a 1-D array instead 
	def generate_random_indices(self, total_number_of_elements):
		self.index_array = array.array('i', range(total_number_of_elements));
		self.index_array_shuffled = array.array('i'); # empty array of integers
		#self.index_array.append(self.index_array[3])
		#print 'array with ordered indices :', self.index_array
		#print 'array index :', self.index_array[2]
		#self.index_array.remove(2);
		#print 'array index :', self.index_array[0]
		range_of_candidate_to_select = total_number_of_elements - 1;
		for x in range(0, (total_number_of_elements)):   # N elements
			# select from the available array of indexes, which is reduced by removing the element selected at every round
			randomCandidate = randint(0, range_of_candidate_to_select) #Inclusive
			#print 'randomCandidate :', randomCandidate
			range_of_candidate_to_select = range_of_candidate_to_select - 1;
			self.index_array_shuffled.append(self.index_array[randomCandidate]);
			self.index_array.remove(self.index_array[randomCandidate]);
		
		#print 'array with ordered indices :', self.index_array		
		print ('array with shuffled indices :', self.index_array_shuffled)
	
	def matrix_to_hex(self, matrix_int, row_size, column_size):
		for x in range(1, (row_size+1)):   # N strings
			for y in range(1, (column_size+1)):  # each M digits
				self.matrix_hex[x-1][y-1] = hex(matrix_int[x-1][y-1]);
		return self.matrix_hex;	
	
	def __del__(self):
		print ("End of data generator life span.\n")
	
####################################
## main
####################################
if __name__ == "__main__":
	id = "< Generator Data >: Internal Agent"
	print ("=====[" + id + " Start]===== \n")
	_lib_object = generator_data(id)
	_lib_object.who_am_i()
	print ("=====[" + id + " End]===== \n");
''''
numberOfRandomStrings = 2; lengthOfDigits = 25; upperBound = 9; lowerBound = 0;
data_generator_object = generator_data();
data_generator_object.generate_random_value(numberOfRandomStrings, lengthOfDigits, upperBound, lowerBound);
print "Printing value for int type.";
data_generator_object.print_matrix_int();

print "\n";

'''