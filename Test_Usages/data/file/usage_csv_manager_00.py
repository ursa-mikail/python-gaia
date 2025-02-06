import os, sys


# point to path
lib_path = os.path.abspath('../../../Libraries/data/file')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)

# import package from path
from csv_manager import csv_manager	# file name
from dataframe_manager import dataframe_manager	#

####################################
## main
####################################
if __name__ == "__main__":
    id_csv_manager = "Usage Agent: Internal Agent <csv_manager>"
    id_dataframe_manager = "Usage Agent: Internal Agent <dataframe_manager>"

    print("=====[" + id_csv_manager + " Start]===== \n")
    print("=====[" + id_dataframe_manager + " Start]===== \n")

    csv_manager_object = csv_manager(id_csv_manager)
    csv_manager_object.who_am_i()
    dataframe_manager_object = dataframe_manager(id_dataframe_manager)

    in_filename = "./test_data/101.pdf"
    file_to_read_from = './test_data/x0.csv'
    file_to_read_from = './test_data/file_to_read_from.csv'

    names, city = [], []
    # row_index = 0;
    column_index = 0;

    # data = csv_manager_object.read_specific_field (file_to_read_from, row_index, column_index)
    number_of_rows = csv_manager_object.get_number_of_rows(file_to_read_from)
    number_of_columns = csv_manager_object.get_number_of_columns(file_to_read_from)

    print("number_of_rows, number_of_columns: ", str(number_of_rows), ', ', str(number_of_columns))
    field_names = csv_manager_object.get_field_names(file_to_read_from)
    print ('field_names: ', field_names)

    row_index = 0;
    for i in range(1, number_of_rows):
        row_index = i
        data = csv_manager_object.read_specific_row(file_to_read_from, row_index)
        name = data[0] + " " + data[1]
        print(name, " lives in ", data[2])


    # write to csv

    # to write to specific field, format the data 1st
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]

    file_to_write_to = "./test_data/out.csv"
    csv_manager_object.write_to_csv(file_to_write_to, data)

    file_to_read_from = './test_data/dataset_00.csv'
    dataframe_object = csv_manager_object.load_data_from_file (file_to_read_from)
    print(dataframe_object)
    column_name = "Buys_Computer"
    [value_elements, data_of_column] = dataframe_manager_object.get_column_data(dataframe_object, column_name)
    print(value_elements)
    print(data_of_column)

    file_to_write_to = "./test_data/out.csv"
    csv_manager_object.write_to_csv(file_to_write_to, data)

    file_to_read_from = './test_data/dataset_01.csv'
    dataframe_object = csv_manager_object.load_data_from_file(file_to_read_from)
    print(dataframe_object)
    column_name = "weather"
    [value_elements, data_of_column] = dataframe_manager_object.get_column_data(dataframe_object, column_name)
    print(value_elements)
    print(data_of_column)

    field_data_to_count = {"weather": 'sunny', "play": 'no'}    # [0, 10]
    # field_data_to_count = {"weather": 'sunny', "play": 'yes'} # [3, 4, 8]
    print("===================")
    for key in field_data_to_count:
        print("key: %s , value: %s" % (key, field_data_to_count[key]))
        column_name, column_value_to_be_counted = key, field_data_to_count[key]
        count = dataframe_manager_object.get_frequency_from_table_given_column_name_and_value(dataframe_object, column_name, column_value_to_be_counted)
        print(count)

    column_name, column_value_to_be_check_with, row_index = "weather", 'sunny', 10
    if(dataframe_manager_object.is_column_value(dataframe_object, column_name, column_value_to_be_check_with, row_index)):
        print("YES")

    column_names_with_values_as_conditions = field_data_to_count
    number_of_conditons_to_check = len(column_names_with_values_as_conditions)
    print(number_of_conditons_to_check)

    row_indices_that_satisfy_conditions = dataframe_manager_object.get_rows_from_table_given_column_names_and_value_as_conditions (dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)

    """
    page_contents_file = "'./data/10-million-combos.txt'";
    keyword_input = 'john';
    keywords_grep_object = keywords_grep.keywords_grep_class(id);
    keywords_grep_object.who_am_i();

    keywords_grep_object.read_contents_and_grep(keyword_input, page_contents_file);

    row_index = 0; 
    column_index = 9;	# DNS
    #column_index = 6;	# port
    data = csv_manager_object.read_specific_field (file_to_read_from, row_index, column_index);	
    print (data);
    row_data = csv_manager_object.get_row (file_to_read_from, row_index);
    print (row_data);
    column_data = csv_manager_object.get_column (file_to_read_from, column_index);
    print (column_data);

    str = column_data[0];
    print(str);

    symbols = ['(', ')', '/']
    str_tokens_filtered = keywords_grep_object.split_with_symbols(str, symbols);
    print (str_tokens_filtered);

    url_protocol_header = "https://"
    target_machine = url_protocol_header + str_tokens_filtered[0] + ":443";
    print(target_machine)
    print(len(target_machine))
    # print(len("https://10.58.91.206:443"))

    # to write to speicific field, format the data 1st
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
        ]
    file_to_write_to = "output.csv"
    csv_manager_object.write_to_csv (file_to_write_to, data)

    # OSError: [Errno 7] Argument list too long, hence, even by doing line based, the line may still be too long.
    # write to file instead.
    file_to_write_to = "./data/target_file.txt"
    target_outfile = open(file_to_write_to, 'w')

    with open(file_to_read_from, 'r') as input_file:
        string_target = input_file.read()
        target_outfile.write(string_target)

    target_outfile.close();

    keyword_input = 'flwekfwlenf';

    page_contents_file = file_to_write_to;
    output_to_display = keywords_grep_object.read_contents_and_grep(keyword_input, page_contents_file);
    if (len(output_to_display) == 0):
        print ("Nothing found");
    else:
        print (output_to_display);

    os.remove(page_contents_file)

    string_target = "abc"

    #sha256_result = keywords_grep_object.compute_sha256_on_string(string_target, "without_whitespaces");
    sha256_result = keywords_grep_object.compute_sha256_on_string(string_target);
    print (sha256_result);	


    with open(file_to_read_from, 'r') as input_file:
        # string_target = input_file.read().replace('\n', '')
        string_target = input_file.read()
        print ("==============================================")
        print (len(string_target))
        output_to_display = keywords_grep_object.grep_string(keyword_input, string_target);
        print (output_to_display);
    """
    # import _Gaia._gaia
    # help(csv_manager) # introspect

    print("=====[" + id_csv_manager + " End]===== \n");
