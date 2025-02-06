# import gaia_construct_main_functions
"""
# point to path
lib_path = os.path.abspath(<gaia_class_path>) # e.g. ('../../Libraries/data')
sys.path.append(lib_path)
"""
# import package from path
from gaia_construct_main_functions import gaia_construct_main	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id_gaia_construct_main = "Usage Agent: <gaia_construct_main>"
    print ("=====[" + id_gaia_construct_main + " Start]===== \n")
    gaia_construct_main_object = gaia_construct_main(id_gaia_construct_main)
    gaia_construct_main_object.who_am_i()
    gaia_construct_main_object.main_menu()
	
    # add procedures

    #import _Gaia._gaia
    #help(gaia_construct_main) # introspect

    print ("=====[" + id_gaia_construct_main + " End]===== \n")

"""
# version: 2018-02-04_1141hr_17sec
"""		