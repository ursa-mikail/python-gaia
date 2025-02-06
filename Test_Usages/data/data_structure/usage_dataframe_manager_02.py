####################################
import os, sys
import numpy as np
import pandas as pd

# point to path
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)

# import package from path
from dataframe_manager import dataframe_manager  # file name

####################################
## main
####################################
if __name__ == "__main__":
    id = "Usage Agent: Agent <dataframe_manager>"
    print("=====[" + id + " Start]===== \n")
    dataframe_manager_object = dataframe_manager(id)

    file_location = '../../../Test_Usages/data/file/test_data/dataset_03.csv'

    dataframe_object = dataframe_manager_object.load_data_from_csv(file_location)
    print(dataframe_object)

    column_headers = dataframe_manager_object.get_column_headers(dataframe_object)
    # print(column_headers)

    [number_of_rows, number_of_columns, number_of_dimensions] = dataframe_manager_object.get_number_of_rows_and_columns_of_dataframe_object(dataframe_object)
    print("number_of_rows, number_of_columns, number_of_dimensions] = ", [number_of_rows, number_of_columns, number_of_dimensions])

    row_index, column_index = 3, 1
    data = dataframe_manager_object.get_data_by_row_and_column_indices(dataframe_object, row_index, column_index)
    print("data: ", data)

    # create another dataframe table
    dataframe_table_name = 'log_table'
    id_log_table = "log"
    dataframe_manager_object_00 = dataframe_manager(id_log_table)
    dataframe_manager_object_00.set_dataframe_object_name(dataframe_table_name)
    """
    
    """
