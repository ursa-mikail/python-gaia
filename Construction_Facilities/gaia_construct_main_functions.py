import time, sys, subprocess
from os.path import abspath, dirname, join

class gaia_construct_main:
	""" Template model of Gaia """
	id = "gaia_construct_main"
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id)
		
	def main_menu(self):
		print("Gaia Utility to Facilitate Code Construction")
		print("===========================================")
		print("")
		self.print_menu()
		
		choice = (input("Choose:\n")) 
		
		if (choice == '1'):
			#cd $source_utility_executable_dir
			#clear; python3 $source_utility_executable
			#printf "Returning to path : "
			#cd -
			print("yet to be done")
		elif (choice == '2'):
			print("yet to be done")
		elif (choice == '3'):
			print("[list_functions]:\n")
			self.list_functions()
		elif (choice == '4'):
			print("yet to be done")         
		elif (choice == '5'):
			print("yet to be done")
		elif (choice == '6'):
			print("yet to be done")
		elif (choice == '7'):
			print("yet to be done")		
		elif ( (choice == 'x') | (choice == 'X') ):
			self.exit_program()
		else:
			self.default_action()
		
		return 
		
	def print_menu(self):
		print("""
		Press 1 : generate_templates_for_python_TDD
		Press 2 : find_functions
		Press 3 : list_functions
		Press 4 : update_then_pack_n_sha_Gaia_and_placed_on_desktop
		Press 5 : open_Gaia_dir
		Press 6 : open_PyCharm_dir
		Press 7 : get_timestamp
		Press 8 : get passcode
		Press 9 : start MongoDB
		Press 10 : back_up_Gaia_OS_to_updates_folder  
		Press 'x' or 'X' to exit the script
		""")
		
		return 		
		
	def list_functions(self):
		file_type = 'py'
		label_start, label_end = 'def ', ':' 

		# command = "find . -regex \".*\.\(" + file_type + "\)\" -type f -exec awk '/" + label_start + "/,/" + label_end + "/ {print }' {} \; | sed -e 's/" + label_start + "/ /g' | sed -e 's/" + label_end + "/ /g'"
		path = abspath(join(dirname(__file__), '../Libraries/'))
		# path = "c://Users/Smita/PycharmProjects/Ursa/ayahuasca/gaia/Construction_Facilities"
		
		# command = r'find . -regex ".*\.' + file_type + r'"' + r" -type f -exec awk '/" + label_start + r"/,/" + label_end + r"/ {print }' {} \; | sed -e 's/" + label_start + r"/ /g' | sed -e 's/" + label_end + r"/ /g'"
		
		command = r'find ' + path + ' -regex ' + r'"' + '*\.' + file_type + r'"' + r" -type f -exec awk '/" + label_start + r"/,/" + label_end + r"/ {print }' {} \; | sed -e 's/" + label_start + r"/ /g' | sed -e 's/" + label_end + r"/ /g'"
		
		command = r'find ' + path + ' -type f -name ' + r'"' + '*.' + file_type + r'"' + r" -exec awk '/" + label_start + r"/,/" + label_end + r"/ {print }' {} \; | sed -e 's/" + label_start + r"/ /g' | sed -e 's/" + label_end + r"/ /g'"		

		command = r'find ' + path + ' -type f -name ' + r'"' + '*.' + file_type + r'"' + r" -exec awk '/" + label_start + r"/,/" + label_end + r"/ {print FILENAME" + r'"' + ':' + r'"' + ' FNR ' + r'"' + ':' + r'"' + " $0}' {} \; | sed -e 's/" + label_start + r"/ /g' | sed -e 's/" + label_end + r"/ /g'"	
		
		# command = r'find ' + path + ' -name ' + r'"' + '*\.' + file_type + r'"' 
		
		# command = 'ps -ef'
		print(command)
		print(path)
		results = subprocess.Popen(command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
		print (results.communicate()[0])

		"""		
		
		"""	

		return
		
	def default_action(self):
		print("""	
		You have entered an invalid selection!
		Please try again!
		""")
		self.main_menu()
		
		return
		
	def exit_program(self):
		sys.exit()
		return
	
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
	id_gaia_construct_main = "Library Agent: Internal Agent <gaia_construct_main>"
	print ("=====[" + id_gaia_construct_main + " Start]===== \n")

	#import _Gaia._gaia
	#help(gaia_construct_main) # introspect

	print ("=====[" + id_gaia_construct_main + " End]===== \n");

"""
# version: 2018-02-04_1041hr_17sec
"""		


"""


"""