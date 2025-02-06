import numpy as np

class display_console:
    """ Template model of Gaia """
    id = "";

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id);

    def print_data_formatted_N_per_row(self, data, data_description, data_per_row):
        print ("\n", "=" * len(data_description), "\n", # header
        data_description, " \n",
        "=" * len(data_description), "\n") # footer
        #print ("[", end ='')

        for i in range(0, len(data)):
            #print (data[i], "\t", end ='')
            print (data[i], ",", end = '')

            if (((i + 1) % data_per_row == 0)):	# every N data next line
                print("")
        #print ("]")

        return

    def get_variable_name_for_display(self, obj, namespace):
        resultant = [name for name in namespace if namespace[name] is obj]
        return resultant[0]

    def display_variable_name_and_value(self, obj, variable):
        print(self.get_variable_name_for_display(variable, obj), ' : ', variable)

        return None

    def display_variable (self, variable_name, variable_value):

        if (variable_name != None):
            print (variable_name, ': ', end='') # variable_name
        else:
            print ("variable_name is non-existent.")

        if (variable_value != None):
            print (variable_value) # display its value
        else:
            print ("variable_value is non-existent.")

        return None

    def display_variable_list (self, variable_name_list, variable_value_list):
        # these 2 numbers should be equal
        number_of_variable_name = len(variable_name_list)
        number_of_variable_value = len(variable_value_list)

        for i in range(0, number_of_variable_name):
            if (variable_name_list[i] != None):
                print (variable_name_list[i], ': ', end='') # variable_name_list
            else:
                print ("variable_name_list is non-existent.")

            if (variable_value_list[i] != None):
                print (variable_value_list[i]) # display its value
            else:
                print ("variable_value_list is non-existent.")

        return None

    def display_matrix (self, matrix_name, matrix):
        space_gap = 50
        row_size, column_size = np.shape(matrix)
        print("============================= ", matrix_name, " =============================")
        print("⌈", " " * space_gap, "⌉")
        for i in range(0, row_size):
            for j in range(0, column_size):
                print(matrix[i][j], "\t", end = "")
            print()
        print()
        print("⌊", " " * space_gap, "⌋")

        return None

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
    id = "Library Agent: Internal Agent <display_console>"
    print ("=====[" + id + " Start]===== \n")
    display_console_object = display_console(id)
    display_console_object.who_am_i()



    #import _Gaia._gaia
    #help(display_console) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-10-20_2214hr_16sec
"""		