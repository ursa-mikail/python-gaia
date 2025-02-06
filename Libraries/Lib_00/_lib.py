'''
This is a Template model of Gaia

to view document introspectively use : 
import _Gaia._gaia
help(_Gaia)
help(_Gaia._gaia)
help(_Gaia._gaia.who_am_i)

or
pydoc _gaia
pydoc _gaia.who_am_i

pydoc _Gaia
pydoc _Gaia._gaia
pydoc _Gaia._gaia.who_am_i

:q to exit

to write to a html:
$ pydoc -w _Gaia
wrote _Gaia.html

'''
####################################
class _lib_class:
	""" Template model of Gaia """
	id = "";
	inventory = {};
	inventory_id = "";
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);

	def init_inventory (self, inventory_id, inventory):
		self.inventory_id = inventory_id;
		self.inventory = inventory;
	
		return;
		
	def inventory_key_exist (self, inventory_key):
		""" check if the key exists """
		found = (inventory_key in self.inventory);

		return found;				
		
	def inventory_item_exist (self, inventory_key, inventory_value):
		values = self.inventory.get(inventory_key)
		
		if (inventory_key in self.inventory):
			if (type(values) is int):				
				if (values == inventory_value):
					return True;
				else:
					return False;
			else:
				number_of_items = len(values);
			
			for i in range(0, number_of_items):
				if (values[i] == inventory_value):
					return True;
			
			print ("item not found")
			return False;	# item not found
		else:
			print ("key not found")
		return;		
		
	def inventory_amend_expand (self, inventory_key, inventory_values):
		self.inventory[inventory_key].extend(inventory_values);
	
		return;		
		
	def inventory_amend_expand_new (self, inventory_key, inventory_values):
		self.inventory[inventory_key] = inventory_values;
	
		return;			
		
	def inventory_amend_contract (self, inventory_key, inventory_values):
		number_of_items_to_remove = len(inventory_values);
		
		for x in range(0, number_of_items_to_remove):
			# find if the item exists in the list
			for i, j in enumerate(self.inventory[inventory_key]):
				if (j == inventory_values[x]): # found
					self.inventory[inventory_key].remove(inventory_values[x]);
					print (inventory_values[x] +  " removed.")
			else:
				print (inventory_values[x] + " not found." )
		return;				

	def inventory_emend_substitute (self, inventory_key, inventory_values_to_be_replaced, inventory_values_to_be_replaced_with):
		number_of_items_to_remove = len(inventory_values_to_be_replaced);
		
		for x in range(0, number_of_items_to_remove):
			# find if the item exists in the list
			for i, j in enumerate(self.inventory[inventory_key]):
				if (j == inventory_values_to_be_replaced[x]): # found
					self.inventory[inventory_key].remove(inventory_values_to_be_replaced[x]);
					self.inventory[inventory_key].append(inventory_values_to_be_replaced_with[x]);
					print (inventory_values_to_be_replaced[x], " removed and replaced with ", inventory_values_to_be_replaced_with[x])
			else:
				print (inventory_values_to_be_replaced[x] + " not found, hence," + inventory_values_to_be_replaced_with[x] + "rejected.")
		return;	
		
	def inventory_module_sort(self, inventory_key):
		self.inventory[inventory_key].sort();
	
		return;		
		
	# yet to be refined
	def inventory_display (self):
		#number_of_items_in_inventory = len(self.inventory);
		
		for key, value in self.inventory.items() :
			print (str(key) + " : " + str(value))
		
		return;	
		
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
	id = "Internal Agent"
	print ("=====[" + id + " Start]===== \n")
	_lib_object = _lib_class(id)
	_lib_object.who_am_i()
	print ("=====[" + id + " End]===== \n");
