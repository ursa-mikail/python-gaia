
# open the file and read each line
places = open( './data/places.txt', 'r' ).readlines()
 
# split by ' -> ', an arrow with spaces
# NB: the .strip() takes the newline '\n' off the end
places = [ str(i.split(' -> ')).strip() for i in places ]

print (places)

###################
def tab_level(astr):
	"""Count number of leading tabs in a string
	"""
	return len(astr)- len(astr.lstrip('\t'))
	
def dict_insert_or_append(adict,key,val):
	"""Insert a value in dict at key if one does not exist
	Otherwise, convert value to list and append
	"""
	if key in adict:
		if type(adict[key]) != list:
			adict[key] = [adict[key]]
		adict[key].append(val)
	else:
		adict[key] = val
		
def ttree_to_json(ttree,level=0):
	result = {}
	for i in range(0,len(ttree)):
		cn = ttree[i]
		try:
			nn  = ttree[i+1]
		except:
			nn = {'level':-1}

		# Edge cases
		if cn['level']>level:
			continue
		if cn['level']<level:
			return result

		# Recursion
		if nn['level']==level:
			dict_insert_or_append(result,cn['name'],cn['value'])
		elif nn['level']>level:
			rr = ttree_to_json(ttree[i+1:], level=nn['level'])
			dict_insert_or_append(result,cn['name'],rr)
		else:
			dict_insert_or_append(result,cn['name'],cn['value'])
		return result
	return result
	
def print_json(json_string):
	number_of_tabs = 0
	
	for i in range(0, len(json_string)):
		if (json_string[i] == '{') | (json_string[i] =='['):
			
			print('')
			
			for j in range(0, number_of_tabs):
				print('\t', end="")
				
			print(json_string[i])
			
			number_of_tabs = number_of_tabs + 1
			
			for j in range(0, number_of_tabs):
				print('\t', end="")
				
		elif (json_string[i] == '}') | (json_string[i] ==']'):
			number_of_tabs = number_of_tabs - 1	
			print('')
			
			for j in range(0, number_of_tabs):
				print('\t', end="")
				
			print(json_string[i], end="")			
		else:
			print(json_string[i], end="")
			
		

	return None
		
	
import json	
# main	
	
#input = open( './data/test.txt', 'r' ).readlines();
#print "\n\ninputs: \n", input;

#for i in input:
#	print "#tabs: ", tab_level(i), " | ", i,

input = [{'name':'person','value':'','level':0},
 {'name':'address','value':'','level':1},
 {'name':'street1','value':'123 Bar St','level':2},
 {'name':'street2','value':'','level':2},
 {'name':'city','value':'Madison','level':2},
 {'name':'state','value':'WI','level':2},
 {'name':'zip','value':55555,'level':2},
 {'name':'web','value':'','level':1},
 {'name':'email','value':'boo@baz.com','level':2}];
	
result_json = ttree_to_json(input);
print ("\n\n", result_json)

result_json = '[' + str(result_json) + ']'

print ("===========================================")
print_json(str(result_json))

#result_json_parsed = json.loads(result_json)
#print json.dumps(result_json_parsed, indent=4, sort_keys=True)