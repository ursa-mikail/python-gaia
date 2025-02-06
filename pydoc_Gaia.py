import os, sys
import subprocess

"""
Recursive pydoc as the 1st step for introspection
Executed at the root of the testbed (for now)
"""
# process_execute
def process_execute(statement):
	hosts = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
	output = hosts.communicate();
	#output_len = len(output);
	output_to_display = str(output[0]).lstrip("b'").rstrip("'"); 
	
	#print (output_to_display);
	#output_array = output_to_display.split("\\r\\n");
	#output_array.remove(''); # remove empty element
	#print (output_array);
		
	return output_to_display
	
def files_found(resultant):
	file_list = resultant.split("\\n")
	
	for i in range(0, len(file_list)): # remove whitespaces
		file_list[i] = file_list[i].replace(" ", "")
		file_list[i] = file_list[i].replace("\\t", "")
		# file_list[i] = file_list[i].replace(".py", "") # remove file extension
		
		if (len(file_list[i]) == 0): # empty item
			file_list.remove(file_list[i])
		
	return file_list	

# print file for now, pydoc recursive disabled not deter pydoc html files populated in the folders
def process_pydoc_recursive(root_starting, file_python_path_list):

	for i in range(0, len(file_python_path_list)): 
		# go to the path
		file_target_path = os.path.dirname(os.path.abspath(file_with_path_list[i]))
		os.chdir(file_target_path)
		
		# remove the path
		file_target_without_path = os.path.basename(file_python_path_list[i])
		file_target_without_path = file_target_without_path.replace(".py", "")
		
		# statement = "pydoc -w " + file_target_without_path 
		# process_execute(statement)
		# print (statement) 
		# return to root_starting
		os.chdir(root_starting)
	
	# find . -name "*.py"
	print ("File found (with path): " + str(file_python_path_list))
	print ("Numbre of Files found (python): " + str(len(file_python_path_list)))
	
	return
	

root_starting = os.getcwd()
print (root_starting)

statement = "find . -name '*.py'";
resultant = process_execute(statement);
file_with_path_list = files_found (resultant)

process_pydoc_recursive(root_starting, file_with_path_list)
"""
print (file_with_path_list)
file_target_path = os.path.dirname(os.path.abspath(file_with_path_list[0]))
print ("file : " + file_with_path_list[0])
print ("file path: " + file_target_path)
"""