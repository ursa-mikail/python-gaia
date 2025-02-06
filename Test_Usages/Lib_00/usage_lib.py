'''
Demonstrating the waking of Gaia
'''
####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/Lib_00')
sys.path.append(lib_path)

# import package from path
import _lib;	# file name

			
####################################
## main
####################################
if __name__ == "__main__":
	id = "Usage Test Agent"
	print ("=====[" + id + " Start]===== \n");

	_gaia_object = _lib._lib_class(id); # file_name.class_name
	_gaia_object.who_am_i();
	
	inventory = {
		'Modules' 		: 10,
		'Journalizing' 	: ['Text', 'Audio'], 
		'backpack' 		: ['xylophone', 'bedroll','bread loaf']
	};
	
	print ("<Before> : %s\n" % _gaia_object.inventory_id)
	print (_gaia_object.inventory)
	
	_gaia_object.init_inventory ("Project `Ayahuasca`", inventory)
	print ("<After initialization> : %s\n" % _gaia_object.inventory_id)
	print (_gaia_object.inventory)
	print ("<After amend expand> : %s\n" % _gaia_object.inventory_id)
	
	_gaia_object.inventory_amend_expand ('Journalizing', ['Image', 'Video'])
	
	print (_gaia_object.inventory)
	print ("<After amend contract> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_amend_contract ('Journalizing', ['Image', 'Video'])
	print (_gaia_object.inventory)
	print ("<After amend contract> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_amend_contract ('Journalizing', ['Image', 'Video'])
	print (_gaia_object.inventory)
	
	inventory_key = 'Journalizing'
	inventory_values_to_be_replaced = ['Image', 'Video'];
	inventory_values_to_be_replaced_with = ['pen', 'paper'];
	print ("<After amend substitute> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_emend_substitute (inventory_key, inventory_values_to_be_replaced, inventory_values_to_be_replaced_with)
	print (_gaia_object.inventory)
	
	print ("try again")
	print ("<After amend expand> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_amend_expand ('Journalizing', ['Image', 'Video'])
	print (_gaia_object.inventory)
	print ("<After amend substitute> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_emend_substitute (inventory_key, inventory_values_to_be_replaced, inventory_values_to_be_replaced_with)
	print (_gaia_object.inventory)
	
	print ("<After amend expand new> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_amend_expand_new ('New', ['Image', 'Video'])
	print (_gaia_object.inventory)
	print ("<After amend expand new> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_amend_expand_new ('Gold', 50)
	print (_gaia_object.inventory)
	
	print ("<After inventory sort> : %s\n" % _gaia_object.inventory_id)
	_gaia_object.inventory_module_sort (inventory_key)
	print (_gaia_object.inventory)
	
	print ("<< Inventory >>")
	print (_gaia_object.inventory_display())
	
	print ("<< Search key in inventory >>")
	inventory_key = "gold";
	print (_gaia_object.inventory_key_exist (inventory_key))
	inventory_key = "Gold";
	print (_gaia_object.inventory_key_exist (inventory_key))
	inventory_value = 60;
	print (_gaia_object.inventory_item_exist (inventory_key, inventory_value))
	inventory_key = "New";
	inventory_value = 60; inventory_value = "Image";
	print (_gaia_object.inventory_item_exist (inventory_key, inventory_value))
	
	print ("=====[" + id + " End]===== \n");
	