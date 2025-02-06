'''

'''
####################################
import csv
import pandas as pd
import os, sys

lib_path = os.path.abspath('../data_structure')
sys.path.append(lib_path)

# import package from path
from dataframe_manager import dataframe_manager	#

class csv_manager:
    """ Template model from Gaia """
    id = ""
    dataframe_object = None
    id_dataframe_manager = "Usage Agent: Internal Agent <dataframe_manager>"
    dataframe_manager_object = None

    def __init__(self, id):
        self.id = id;
        print("csv_data_extractor object [%s] is born\n" % self.id)
        self.dataframe_manager_object = dataframe_manager(self.id_dataframe_manager)

    def who_am_i(self):  # read from file
        """ Introspection """
        self.line_storage = [];

        print("My name is csv_data_extractor [", self.id, "].")

        return

    """
    Read and load data
    """		
    def load_csv_into_list(self, file_to_read_from):
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            data_list = []

            for row in csv_table:
                data_list.append(row)  # append data into list

        return data_list

    def load_data_from_file (self, file_to_read_from):
        self.dataframe_object = pd.read_csv(file_to_read_from, sep=',', header=(0)) # no header
        return self.dataframe_object

    def get_row(self, file_to_read_from, row_index):  # to-do: set_row
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            row_counter = 0

            for row in csv_table:
                if (row_counter == row_index):
                    row_data = row  # get row_data at row_index
                    break

                row_counter = row_counter + 1

        csvfile.close();

        return row_data

    def get_column(self, file_to_read_from, column_index):  # to-do: set_column
        column_data = [];

        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            for row in csv_table:
                column_data.append(row[column_index])  # get data field at column_index of the row

        csvfile.close();

        return column_data;

    def read_specific_field(self, file_to_read_from, row_index, column_index):
        print("enter function read_specific_field")
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            row_counter = 0;

            for row in csv_table:
                # print ("row counter is", row_counter)
                # print("row ", row)
                if (row_counter == row_index):
                    data = row[column_index]  # get column at column_index
                    # print ("data is", data)
                    break;

                row_counter = row_counter + 1;

        csvfile.close();

        return data;

    def read_specific_row(self, file_to_read_from, row_index):
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            row_counter = 0;

            for row in csv_table:
                # print ("row counter is", row_counter)
                # print ("row ", row)
                if (row_counter == row_index):
                    data = row
                    # print ("data is", data)
                    break;

                row_counter = row_counter + 1

        csvfile.close()

        return data

    # assume 1st row contain fields
    def csv_to_dictionary(self, file_to_read_from):
        number_of_rows = self.get_number_of_rows(file_to_read_from)
        number_of_columns = self.get_number_of_columns(file_to_read_from)   # number_of_fields

        fields = self.get_row(file_to_read_from, row_index = 0)# get from 1st row
        # data_dictionary = {}
        columns_of_data = []

        for column_index in range(0, number_of_columns):
            columns_of_data.append(self.get_column(file_to_read_from, column_index))

        # to-do: omit the 1st row

        list_with_keys, list_with_values = fields, columns_of_data
        data_dictionary = dict(zip(list_with_keys, list_with_values))

        # print(data_dictionary)

        return data_dictionary

    """
    Profiling
    """			
    def get_number_of_rows(self, file_to_read_from):
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            row_counter = 0

            for row_data in csv_table:
                if(self.row_data_is_empty(row_data) != True):
                    row_counter = row_counter + 1

        csvfile.close()

        return row_counter

    def get_number_of_columns(self, file_to_read_from):
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            for row_data in csv_table:
                column_counter = len(row_data)
                # just get the 1st read and exit from break
                break

        csvfile.close()

        return column_counter

    def get_number_of_columns_of_csv_given_row_index (self, file_to_read_from, row_index):

        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            row_counter = 0;

            for row in csv_table:
                if (row_counter == row_index):
                    data = row
                    break;

                row_counter = row_counter + 1;

        csvfile.close();

        row_data = str(data).split(",")
        print("row_data: ", row_data)

        return len(row_data)		

    def get_field_names (self, file_to_read_from):
        with open(file_to_read_from, "r") as csvfile:
            csv_table = csv.reader(csvfile, delimiter=',')

            for row_data in csv_table:
                field_names = row_data # type is list
                # just get the 1st read and exit from break
                break

        csvfile.close()

        return field_names

    def row_data_is_empty(self, row_data):
        # row_data is list
        if (len(row_data) == 0):
            return True

        return False

    """
    Processing
    """	
    def filter_out_by_keywords_specified_column_index (self, target_csv_file, key_word_list, column_index):
        DOES_NOT_EXIST, EXIST = -1, 1
        STATUS = DOES_NOT_EXIST
        data_list_filtered = []

        data_list = self.load_csv_into_list(target_csv_file)

        for i in range(0, len(data_list)):

            if (column_index <= i): # check if the field specified by the column index exists

                for j in range(0, len(key_word_list)):
                    target_row_data = data_list[i]

                    if target_row_data[column_index].find(key_word_list[j]) == DOES_NOT_EXIST:
                        pass;
                    else:
                        STATUS = EXIST
                        break

                if (STATUS == DOES_NOT_EXIST):
                    data_list_filtered.append(data_list[i])

                STATUS = DOES_NOT_EXIST # reset flag for the next scan

        return data_list_filtered

    """
    for line_num, (is_last, row) in enumerate(isLast(reader)):
        if not is_last: assert len(row) == len(header)	
    """

    def separate_1st_N_rows_into_1_file_and_rest_in_another (self, target_csv_file_in, csv_file_1st_N_rows_out, csv_file_rest_of_the_rows_out, N_rows_to_be_extracted):
        data_list_full = self.load_csv_into_list(target_csv_file_in)

        number_of_rows = len(data_list_full)

        if (N_rows_to_be_extracted >= number_of_rows):
            print('N_rows_to_be_extracted > number_of_rows: No file output.')

        else:
            data_list_1st_N_rows = data_list_full[0:N_rows_to_be_extracted]
            data_list_rest_of_the_rows = data_list_full[N_rows_to_be_extracted:len(data_list_full)]

            self.write_to_csv(csv_file_1st_N_rows_out, data_list_1st_N_rows)
            self.write_to_csv(csv_file_rest_of_the_rows_out, data_list_rest_of_the_rows)

        return		

    def delete_rows_from_row_i_to_row_j_from_target_file(self, file_to_read_from, file_to_write_to, row_i, row_j):

        offset_from_zero = - 1
        contents = self.load_csv_into_list (file_to_read_from)
        number_of_rows = len(contents)

        if (number_of_rows < row_i) | (number_of_rows < row_j):
            print('File has ', number_of_rows, ' not able to truncate row ', row_i, ' to row ', row_j)
        else:
            del contents[(row_i + offset_from_zero):(row_j + 1 + offset_from_zero)]
            self.write_to_csv (file_to_write_to, contents)

        return

    def delete_columns_from_column_i_to_column_j_from_target_file(self, file_to_read_from, file_to_write_to, column_i, column_j):

        offset_from_zero = - 1
        contents = self.load_csv_into_list (file_to_read_from)
        number_of_rows = len(contents)
        contents_with_filtered_columns = []

        FILTERING_COMPLETED, FILTERING_INCOMPLETE = True, False
        STATUS = FILTERING_INCOMPLETE

        for i in range(0, number_of_rows):
            number_of_columns = len(contents[i])
            # print(number_of_columns)

            if (number_of_columns < column_i) | (number_of_columns < column_j):
                print('File has ', number_of_columns, ' columns. Not able to truncate column ', column_i, ' to column ', column_j)
                STATUS = FILTERING_INCOMPLETE
                return STATUS
            else:
                row_content_to_be_filtered = contents[i]
                del row_content_to_be_filtered[(column_i + offset_from_zero):(column_j + 1 + offset_from_zero)]
                contents_with_filtered_columns.append(row_content_to_be_filtered)


        self.write_to_csv(file_to_write_to, contents_with_filtered_columns)
        STATUS = FILTERING_COMPLETED

        return STATUS

    """
    Write data to a CSV file path
    """

    def write_to_csv(self, file_to_write_to, data):
        with open(file_to_write_to, "w", newline='') as csvfile:
            csv_table = csv.writer(csvfile, delimiter=',')
            for line in data:
                csv_table.writerow(line)

        csvfile.close();

        return None

    def format_data_for_writing(self, field_data=None, column_data_object_list=None):
        if (field_data != None):
            # write field descriptions to csv
            string_field = ","  # with index
            # string_field = "" # without index

            for i in range(0, len(field_data)):
                string_field = string_field + field_data[i] + ","

            string_field.rstrip(",");  # remove last ","
            formatted_csv_data = [string_field.split(","), ]
        else:
            formatted_csv_data = [];

        # to do: check column_data_object_list
        # 1. total objects in the list has some number of fields as field_data
        # 2. all objects on the list has the same number of row elements
        # 3. column_data_object_list is not empty

        number_of_objects_in_column_data_object_list = len(column_data_object_list)
        number_of_row_data = len(column_data_object_list[0])  # use 1st object as reference
        # format data for writing to csv
        for i in range(0, number_of_row_data):
            row_data = str(i + 1)  # with index
            # row_data = "" # without index

            for j in range(0, number_of_objects_in_column_data_object_list):
                # row_data = str(str(i+1) + "," + IP_hostnames[i] + "," + ports[i]).split(",")
                object_in_list = column_data_object_list[j]
                row_data = row_data + "," + object_in_list[i]

            row_data = str(row_data).split(",")

            formatted_csv_data.append(row_data)

        return formatted_csv_data

    # fields in the 1st column for this function (to-do: to be transposed)
    def dictionary_to_csv(self, data_dictionary, file_to_write_to):
        fields = []
        columns_of_data = []
        for key, value in data_dictionary.items():  # Iterates through the pairs
            # print(key, ":", value)
            fields.append(key)
            columns_of_data.append(value)

        data = []
        column_0 = columns_of_data[0]
        number_of_rows = len(column_0)

        # print("number_of_rows: ", number_of_rows)

        line = ''
        for i in range(0, number_of_rows):
            line = ''
            for j in range(0, len(fields)):
                column_item = columns_of_data[j]
                line += column_item[i]

                #if j != len(fields):
                #    line += ','

            data.append(line)

        data = columns_of_data
        self.write_to_csv(file_to_write_to, data)

        return

    def __del__(self):
        print("csv_data_extractor object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id_csv_manager = "Library Agent: Internal Agent <csv_manager>"
    print("=====[" + id_csv_manager + " Start]===== \n")
    csv_manager_object = csv_manager(id_csv_manager)
    # csv_manager_object.who_am_i();

    file_to_read_from = '../../../Test_Usages/data/file/test_data/dataset_03.csv'
    data_dictionary = csv_manager_object.csv_to_dictionary(file_to_read_from)

    """
    for key in data_dictionary:  # Iterates just through the keys, ignoring the values
        print(key)
    for key, value in data_dictionary.items():  # Iterates through the pairs
        print(key, ":", value)
    for key in data_dictionary.keys():  # Iterates just through key, ignoring the values
        print(key)
    for value in data_dictionary.values():  # Iterates just through value, ignoring the keys
        print(value)
    """

    file_to_write_to = '../../../Test_Usages/data/file/test_data/dataset_04.csv'
    csv_manager_object.dictionary_to_csv(data_dictionary, file_to_write_to)

    # import _Gaia._gaia
    # help(csv_manager) # introspect

    print("=====[" + id_csv_manager + " End]===== \n");
