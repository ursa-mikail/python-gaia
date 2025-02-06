import pandas as pd

#
class dataframe_manager:
    """ Template model of Gaia """
    id = "dataframe_manager";
    inventory = {};
    dataframe_manager_id = ""

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id)

    def set_dataframe_object_name(self, dataframe_manager_id):
        self.dataframe_manager_id = dataframe_manager_id

        return None

    def get_dataframe_object_name(self):

        return self.dataframe_manager_id

    def load_data_from_csv (self, file_location):
        dataframe_object = pd.read_csv(file_location, quotechar="'") # sep=',', escapechar='\\') #
        return dataframe_object

    # create dataframe table with array with_row_names_and_column_names in the array or matrix
    def create_dataframe_object_with_data_table_N_by_M_with_row_names_and_column_names (self, data_table_values_N_by_M_with_row_names_and_column_names):
        row_names, column_names = data_table_values_N_by_M_with_row_names_and_column_names[1:, 0], data_table_values_N_by_M_with_row_names_and_column_names[0, 1:]  # at [row 1 onwards , column 0], [row 0, column 1 onwards]

        data_table_values_N_by_M = data_table_values_N_by_M_with_row_names_and_column_names[1:, 1:]  # start from [1, 1], “:” means onwards

        dataframe_object = pd.DataFrame(data = data_table_values_N_by_M, index = row_names, columns = column_names)

        return dataframe_object

    # create dataframe table with array without given row_names_and_column_names in the array or matrix
    def create_dataframe_object_with_data_table_N_by_M_without_row_names_and_column_names(self, data_table_values_N_by_M, row_names, column_names):
        # data_table_values_N_by_M = data_table_values_N_by_M_without_row_names_and_column_names
        dataframe_object = pd.DataFrame(data = data_table_values_N_by_M, index = row_names, columns = column_names)

        return dataframe_object

    def get_column_headers (self, dataframe_object):
        column_headers = list(dataframe_object)
        return column_headers

    def get_column_index_given_column_label(self, dataframe_object, column_field_label):
        column_headers = self.get_column_headers(dataframe_object)
        column_index = column_headers.index(column_field_label)
        return column_index
	
    def get_unique_values_of_fields_under_column(self, dataframe_object, column_name):
        value_elements_unique = list(set(dataframe_object[column_name]))
        return value_elements_unique

    def count_frequencies_of_unique_values(self, dataframe_object, column_name): # histogram
        value_elements_unique = self.get_unique_values_of_fields_under_column(dataframe_object, column_name)
        number_of_values_elements_unique = len(value_elements_unique)
        frequency_of_value_elements_unique = [None]*number_of_values_elements_unique

        for i in range(0, number_of_values_elements_unique):
            column_value_to_be_counted = value_elements_unique[i]
            frequency_of_value_elements_unique[i]= self.get_frequency_from_table_given_column_name_and_value (dataframe_object, column_name, column_value_to_be_counted)


        return [value_elements_unique, frequency_of_value_elements_unique]

    def get_column_data (self, dataframe_object, column_name):
        value_elements = list(set(dataframe_object[column_name]))
        data = list(dataframe_object[column_name])
        return [value_elements, data]

    def write_data_to_csv (self, headers, data, file_location):
        dataframe_object = pd.DataFrame(data, columns = headers) # dataframe_object.to_csv(file_location, sep='\t') or dataframe_object.to_csv(file_location, sep='\t', encoding='utf-8') # .. , index=False)
        dataframe_object.to_csv(file_location, index = False)

        return None

    def write_dataframe_to_csv (self, dataframe_object, file_location):
        dataframe_object.to_csv(file_location)

        return None
		
    def get_number_of_rows_and_columns_of_dataframe_object(self, dataframe_object):
        number_of_dimensions = len(dataframe_object.shape)

        if (number_of_dimensions == 2):
            number_of_rows = dataframe_object.shape[0]
            number_of_columns = dataframe_object.shape[1]
        else:
            print("Number_of_dimensions < 2")

        return [number_of_rows, number_of_columns, number_of_dimensions]

    def get_dataframe_headers (self, dataframe_object):
        headers_dataframe = dataframe_object.columns.values.tolist()

        return headers_dataframe

    def get_dataframe_row (self, dataframe_object, row_number):
        dataframe_matrix = self.dataframe_object_to_matrix(dataframe_object)

        row_content = dataframe_matrix[row_number,:] # get row_content

        return row_content

    def get_dataframe_column (self, dataframe_object, column_number):
        dataframe_matrix = self.dataframe_object_to_matrix(dataframe_object)
        column_content = dataframe_matrix[:, column_number] # get column_content

        return column_content

    # exclude headers if it exist
    def get_data_by_row_and_column_indices (self, dataframe_object, row_index, column_index):
        data_in_field = dataframe_object.iloc[row_index][column_index] # Using `iloc[]`, i.e. row and column indices

        return data_in_field

    def get_data_by_row_and_column_names (self, dataframe_object, row_name, column_name):
        # data_in_field = dataframe_object.loc[row_name][column_name] # # Using `loc[]`, i.e. row and column names
        data_in_field = dataframe_object.at[row_name, column_name]  # Using `at[]`, i.e. row and column names

        return data_in_field

    def dataframe_object_to_matrix (self, dataframe_object):
        # dataframe_object_as_matrix = dataframe_object.as_matrix()
        dataframe_object_as_matrix = dataframe_object.values

        return dataframe_object_as_matrix

    def is_column_value(self, dataframe_object, column_name, column_value_to_be_check_with, row_index):
        data_under_column_name = list(dataframe_object[column_name])
        assert ((row_index + 1) <= len(data_under_column_name)), "Row index exceeds row size"

        if (data_under_column_name[row_index] == column_value_to_be_check_with):
            return True
        else:
            return False

       # return None

    def get_rows_from_table_given_column_names_and_value_as_conditions(self, dataframe_object, column_names_with_values_as_conditions):
        row_indices_that_satisfy_conditions = []
        # hit_all_conditions = False
        count_conditions = len(column_names_with_values_as_conditions)  # length of dictionary
        count_hit = 0

        # row by row, check all conditions (AND)
        for row_index in range(0, len(dataframe_object)):
            for key in column_names_with_values_as_conditions:
                # print("key: %s , value: %s" % (key, column_names_with_values_as_conditions[key]))
                column_name, column_value_to_be_check_with = key, column_names_with_values_as_conditions[key]
                data_under_column_name = list(dataframe_object[column_name])

                if (self.is_column_value(dataframe_object, column_name, column_value_to_be_check_with, row_index)):
                    count_hit += 1

            if (count_hit == count_conditions):  # hit_all_conditions = True
                row_indices_that_satisfy_conditions.append(row_index)

            count_hit = 0  # reset counter

        return row_indices_that_satisfy_conditions

    def get_frequency_from_table_given_column_name_and_value (self, dataframe_object, column_name, column_value_to_be_counted):
        data_under_column_name = list(dataframe_object[column_name])
        count = 0
        for i in range(0, len(data_under_column_name)):
            if (data_under_column_name[i] == column_value_to_be_counted):
                count += 1
        return count
		
    def sort_by_column_field_and_get_sorted_row_indices(self, dataframe_object, column_field_label):
        dataframe_object_sorted = dataframe_object[column_field_label].to_frame().sort_values(column_field_label, ascending=False)

        row_indices_sorted = []
        number_of_row_indices = len(dataframe_object_sorted.iloc[:, ])
        # print("number_of_row_indices: ", number_of_row_indices)

        for i in range(0, number_of_row_indices):  # get sorted indices
            row_indices = dataframe_object_sorted.iloc[i,].name  # dataframe_object_sorted.columns
            row_indices_sorted.append(row_indices)

        return row_indices_sorted

	# can also be done via : dataframe_object_sorted = dataframe_object.reindex(row_indices_sorted)
    def sort_dataframe_object_given_row_indices(self, dataframe_object, row_indices):
        dataframe_object_sorted = dataframe_object.copy()
        row_size, column_size = dataframe_object.shape

        for i in range(0, row_size):
            dataframe_object_sorted.iloc[i] = dataframe_object.iloc[row_indices[i]]

        return dataframe_object_sorted		

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
    id = "Library Agent: Internal Agent <dataframe_manager>"
    print ("=====[" + id + " Start]===== \n")
    dataframe_manager_object = dataframe_manager(id)
    dataframe_manager_object.who_am_i()

    file_location = 'https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv'
    file_location = '../../../Test_Usages/data/test_data/pml-training.csv'

    dataframe_object = dataframe_manager_object.load_data_from_csv (file_location)

    [number_of_rows, number_of_columns, number_of_dimensions] = dataframe_manager_object.get_number_of_rows_and_columns_of_dataframe_object(dataframe_object)
    print(number_of_rows, number_of_columns, number_of_dimensions)

    dataframe_matrix = dataframe_manager_object.dataframe_object_to_matrix(dataframe_object)
    print(dataframe_matrix)

    headers_dataframe = dataframe_manager_object.get_dataframe_headers (dataframe_object)
    print (headers_dataframe)

    # data_format
    meta_data_tags = ['slot_space_id', 'session_id', 'secret',
            'work_space', 'work_space_state']

    work_space_states_defined = ['dead', 'initialized', 'create', 'active', 'suspended', 'terminated']	# dead -> initialized (birth) -> create (designated) -> active -> suspended -> terminated (destroyed, to be returned to `dead` state)

    template = {meta_data_tags[0]: [],
            meta_data_tags[1]: [], # zero is not allowed, it only means to be assigned / unassigned
            meta_data_tags[2]: [],
            meta_data_tags[3]: [],
            meta_data_tags[4]: [],
            }

    # data
    list_slot_space_id = ['ursa', 'coco', 'kiss', 'hope']
    list_session_id = [0x5a5a, 0x1001, 0xbabe, 0xbab4]
    list_secret = ['to-see', 'hop-hop', 'tokyo', 'full-metal']
    list_work_space = [[0, 0xfe, 0xff], [0xca, 0xfe], [0xf0, 0x0d], [0xde, 0xed, 0x01]]
    list_work_space_state = [work_space_states_defined[0], work_space_states_defined[1], work_space_states_defined[3], work_space_states_defined[4]]

    number_of_entries = len(list_slot_space_id)

    number_of_meta_tags = len(meta_data_tags);

    for i in range(0, number_of_entries):
        template[meta_data_tags[0]].append(list_slot_space_id[i])	# 'slot_space_id'
        template[meta_data_tags[1]].append(list_session_id[i])			# session_id
        template[meta_data_tags[2]].append(list_secret[i]);			# secret
        template[meta_data_tags[3]].append(list_work_space[i])	# work_space
        template[meta_data_tags[4]].append(list_work_space_state[i])	# work_space_state

    print ([template[x] for x in meta_data_tags])

    file_location = '../../../Test_Usages/data/test_data/out.csv'

    data = template
    headers = meta_data_tags

    dataframe_manager_object.write_data_to_csv (headers, data, file_location)

    #import _Gaia._gaia
    #help(dataframe_manager) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2018-03-14_1844hr_49sec
"""

"""
# Single selections using iloc and DataFrame
# Rows:
data.iloc[0] # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
data.iloc[1] # second row of data frame (Evan Zigomalas)
data.iloc[-1] # last row of data frame (Mi Richan)
# Columns:
data.iloc[:,0] # first column of data frame (first_name)
data.iloc[:,1] # second column of data frame (last_name)
data.iloc[:,-1] # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
data.iloc[0:5] # first five rows of dataframe
data.iloc[:, 0:2] # first two columns of data frame with all rows
data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
data.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

# Select rows with first name Antonio, # and all columns between 'city' and 'email'
data.loc[data['first_name'] == 'Antonio', 'city':'email']
 
# Select rows where the email column ends with 'hotmail.com', include all columns
data.loc[data['email'].str.endswith("hotmail.com")]   
 
# Select rows with last_name equal to some values, all columns
data.loc[data['first_name'].isin(['France', 'Tyisha', 'Eric'])]   
       
# Select rows with first name Antonio AND hotmail email addresses
data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')] 
 
# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']] 
 
# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
data.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)] 
 
# Selections can be achieved outside of the main .loc for clarity:
# Form a separate variable with your selections:
idx = data['company_name'].apply(lambda x: len(x.split(' ')) == 4)
# Select only the True values in 'idx' and only the 3 columns specified:
data.loc[idx, ['email', 'first_name', 'company']]

"""