####################################
import os, sys
import numpy as np
import pandas as pd

# point to path
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)

# import package from path
from dataframe_manager import dataframe_manager	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id = "Usage Agent: Agent <dataframe_manager>"
    print ("=====[" + id + " Start]===== \n")
    dataframe_manager_object = dataframe_manager(id)
    dataframe_manager_object.who_am_i()

    file_location = 'https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv'
    file_location = '../../../Test_Usages/data/test_data/pml-training.csv'
    file_location = '../../../Test_Usages/data/file/test_data/dataset_00.csv'

    dataframe_object = dataframe_manager_object.load_data_from_csv (file_location)

    [number_of_rows, number_of_columns, number_of_dimensions] = dataframe_manager_object.get_number_of_rows_and_columns_of_dataframe_object(dataframe_object)
    print(number_of_rows, number_of_columns, number_of_dimensions)

    dataframe_matrix = dataframe_manager_object.dataframe_object_to_matrix(dataframe_object)
    print(dataframe_matrix)

    # headers_dataframe = dataframe_manager_object.get_dataframe_headers (dataframe_object)
    #print (headers_dataframe)

    row_number = 0
    column_number = 0

    row_content = dataframe_manager_object.get_dataframe_row (dataframe_object, row_number)
    print(row_content)

    column_content = dataframe_manager_object.get_dataframe_column (dataframe_object, column_number)
    print(column_content)

    print(dataframe_object)

    row_index, column_index = 1, 3
    data_in_field = dataframe_manager_object.get_data_by_row_and_column_indices(dataframe_object, row_index, column_index)
    print("data_in_field = ", data_in_field)
    row_name, column_name = 0, 'Credit_Rating'
    data_in_field = dataframe_manager_object.get_data_by_row_and_column_names(dataframe_object, row_name, column_name)
    print("data_in_field = ", data_in_field)

    value_elements_unique = dataframe_manager_object.get_unique_values_of_fields_under_column(dataframe_object, column_name)
    print(value_elements_unique)
    column_headers = dataframe_manager_object.get_column_headers(dataframe_object)
    print(column_headers)

    [value_elements_unique, frequency_of_value_elements_unique] = dataframe_manager_object.count_frequencies_of_unique_values(dataframe_object, column_name)  # histogram

    print([value_elements_unique, frequency_of_value_elements_unique])

    column_headers, row_headers = ['', 'Col1', 'Col2', 'Col3'], ['Row1', 'Row2', 'Row3']
    # option 1: create dataframe table with array with_row_names_and_column_names in the array or matrix
    data_table_values_N_by_M_with_row_names_and_column_names = np.array(
        [column_headers,  # with row names or column names
         [row_headers[0], 1, 2, 7],
         [row_headers[1], 3, 4, 11],
         [row_headers[2], 5, 5, 11]])

    x, y = 1, 1
    data_table_values_N_by_M_with_row_names_and_column_names[x][y] = 22
    print(data_table_values_N_by_M_with_row_names_and_column_names[x][y])

    dataframe_object = dataframe_manager_object.create_dataframe_object_with_data_table_N_by_M_with_row_names_and_column_names(data_table_values_N_by_M_with_row_names_and_column_names)
    print(dataframe_object)

    # option 2: create dataframe table with array without given row_names_and_column_names in the array or matrix
    data_table_values_N_by_M = np.array([  # without row names or column names
        [1, 2, 7],
        [3, 4, 11],
        [5, 5, 11]])

    x, y = 1, 1
    print(data_table_values_N_by_M[x][y])

    row_names, column_names = row_headers, column_headers[1:]
    # create dataframe table
    dataframe_object = dataframe_manager_object.create_dataframe_object_with_data_table_N_by_M_without_row_names_and_column_names(data_table_values_N_by_M, row_names, column_names)
    print(dataframe_object)

    print(dataframe_manager_object.get_data_by_row_and_column_indices (dataframe_object, x, y))

    #import _Gaia._gaia
    #help(dataframe_manager) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-09-23_2010hr_04sec
"""	