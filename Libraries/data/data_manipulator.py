import numpy as np


# data is re-arranged by this module
class data_manipulator:
    """ Template model of Gaia """
    id = "data_manipulator";
    inventory = {};
    inventory_id = "";

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id);

    def get_array_matrix_dimensions(self, array_or_matrix):
        return np.shape(array_or_matrix)

    def array_or_matrix_dimensions_are_same (self, array_or_matrix_00, array_or_matrix_01):
        array_or_matrix_00_dimensions = self.get_array_matrix_dimensions(array_or_matrix_00)
        array_or_matrix_01_dimensions = self.get_array_matrix_dimensions(array_or_matrix_01)

        if (array_or_matrix_00_dimensions == array_or_matrix_01_dimensions):
            return True
        else:
            return False

    #
    def create_list_to_array (self, data_type, list_of_values):
        data_type_format = np.float_
        if (data_type == 'float'):
            data_type_format = np.float_
        if (data_type == 'int'):
            data_type_format = np.int_

        array_N = np.array(list_of_values, dtype = data_type_format)

        return array_N

    def create_list_to_matrix (self, data_type, list_of_values):
        data_type_format = np.float_
        if (data_type == 'float'):
            data_type_format = np.float_
        if (data_type == 'int'):
            data_type_format = np.int_

        matrix_NxM = np.array(list_of_values, dtype = data_type_format)

        return matrix_NxM

    # fill with indices starting with 0
    def create_array_N (self, N, data_type, zeroized_flag = False):
        data_type_format = np.float_
        if (data_type == 'float'):
            data_type_format = np.float_
        if (data_type == 'int'):
            data_type_format = np.int_

        if (zeroized_flag == False):
            array_N = np.array(np.arange(N, dtype = data_type_format))
        else:
            array_N = np.zeros((N,), dtype = data_type_format)

        return array_N

    # fill with indices starting with 0
    def create_matrix_NxM (self, N, M, data_type, zeroized_flag = False):
        data_type_format = np.float_
        if (data_type == 'float'):
            data_type_format = np.float_
        if (data_type == 'int'):
            data_type_format = np.int_

        if (zeroized_flag == False):
            array = np.arange((N*M), dtype = data_type_format)
            matrix_NxM = array.reshape(N,M)
        else:
            matrix_NxM = np.zeros((N,M), dtype = data_type_format)

        return matrix_NxM

    def shuffle_array(self, array_unshuffled, indices_shuffled): #
        # assume: len(array_unshuffled) == len(indices_shuffled)
        array_shuffled = []

        for i in range(0, len(indices_shuffled)):
            index_pointed = indices_shuffled[i]
            array_shuffled.append(array_unshuffled[index_pointed])

        return array_shuffled

    def unshuffle_array(self, array_shuffled, indices_shuffled_as_lookup): #
        # assume: len(array_shuffled) == len(indices_shuffled_as_lookup)
        # filled up with same type of data, let's use the same array
        array_unshuffled = []
        for i in range(0, len(indices_shuffled_as_lookup)):
            array_unshuffled.append(array_shuffled[i])

        # unscramble now
        for i in range(0, len(indices_shuffled_as_lookup)):
            index_pointed = indices_shuffled_as_lookup[i]
            array_unshuffled[index_pointed] = array_shuffled[i]

        return array_unshuffled

    # each record holds n-tuple [(...), .... ,(...)]
    def sort_record_tuple_list (self, record_tuple_list, sort_by_nth_item, ascending_mode = False):

        if (ascending_mode == True):
            record_tuple_list_sorted = sorted(record_tuple_list, key = lambda score: score[sort_by_nth_item]) # ascending
        else:
            record_tuple_list_sorted = sorted(record_tuple_list, key=lambda score: score[sort_by_nth_item], reverse=True)  # descending

        return record_tuple_list_sorted

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
    id = "Library Agent: Internal Agent <data_manipulator>"
    print ("=====[" + id + " Start]===== \n")
    data_manipulator_object = data_manipulator(id)
    data_manipulator_object.who_am_i()

    a = np.arange(9, dtype = np.float_).reshape(3,3)
    print(a)

    zeroized_flag = True
    # a = np.arange(9, dtype = np.float_).reshape(3,3)
    N, M, data_type = 5, 8, 'float' # 'int'
    matrix_NxM = data_manipulator_object.create_matrix_NxM (N, M, data_type, zeroized_flag)
    print(matrix_NxM)
    array_N = data_manipulator_object.create_array_N (N, data_type, zeroized_flag)
    print(array_N)

    list_of_values = [10, 9, 10]
    array_N = data_manipulator_object.create_list_to_array (data_type, list_of_values)
    print(array_N)

    list_of_values = [[3,7,5],[8,4,3],[2,4,9]]
    matrix_NxM = data_manipulator_object.create_list_to_matrix(data_type, list_of_values)
    print(matrix_NxM)




    #import _Gaia._gaia
    #help(data_manipulator) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-09-23_2010hr_04sec
"""		