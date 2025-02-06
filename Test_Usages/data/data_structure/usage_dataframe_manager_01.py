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

    file_location = '../../../Test_Usages/data/file/test_data/dataset_01.csv'

    dataframe_object = dataframe_manager_object.load_data_from_csv(file_location)
    print(dataframe_object)

    column_headers = dataframe_manager_object.get_column_headers(dataframe_object)
    print(column_headers)

    column_name = column_headers[1]
    [value_elements_unique, frequency_of_value_elements_unique] = dataframe_manager_object.count_frequencies_of_unique_values(dataframe_object,
                                                                                                       column_name)  # histogram
    print([value_elements_unique, frequency_of_value_elements_unique])
    column_name = column_headers[0]
    [value_elements_unique, frequency_of_value_elements_unique] = dataframe_manager_object.count_frequencies_of_unique_values(dataframe_object,
                                                                                                       column_name)  # histogram
    print([value_elements_unique, frequency_of_value_elements_unique])

    # create another dataframe table
    dataframe_table_name = 'frequency_table'
    id_frequency_table = "Usage Agent: Agent <dataframe_manager>: [" + dataframe_table_name + "]"
    print("=====[" + id_frequency_table + " Start]===== \n")
    dataframe_manager_object_00 = dataframe_manager(id_frequency_table)
    dataframe_manager_object_00.set_dataframe_object_name(dataframe_table_name)

    column_names_with_values_as_conditions = {"weather": 'overcast', "play": 'yes'}
    row_indices_that_satisfy_conditions = dataframe_manager_object_00.get_rows_from_table_given_column_names_and_value_as_conditions(dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)
    column_names_with_values_as_overcast_and_yes = len(row_indices_that_satisfy_conditions)

    column_names_with_values_as_conditions = {"weather": 'overcast', "play": 'no'}
    row_indices_that_satisfy_conditions = dataframe_manager_object_00.get_rows_from_table_given_column_names_and_value_as_conditions(
        dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)
    column_names_with_values_as_overcast_and_no = len(row_indices_that_satisfy_conditions)

    column_names_with_values_as_conditions = {"weather": 'rainy', "play": 'yes'}
    row_indices_that_satisfy_conditions = dataframe_manager_object_00.get_rows_from_table_given_column_names_and_value_as_conditions(dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)
    column_names_with_values_as_rainy_and_yes = len(row_indices_that_satisfy_conditions)

    column_names_with_values_as_conditions = {"weather": 'rainy', "play": 'no'}
    row_indices_that_satisfy_conditions = dataframe_manager_object_00.get_rows_from_table_given_column_names_and_value_as_conditions(dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)
    column_names_with_values_as_rainy_and_no = len(row_indices_that_satisfy_conditions)

    column_names_with_values_as_conditions = {"weather": 'sunny', "play": 'yes'}
    row_indices_that_satisfy_conditions = dataframe_manager_object_00.get_rows_from_table_given_column_names_and_value_as_conditions(dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)
    column_names_with_values_as_sunny_and_yes = len(row_indices_that_satisfy_conditions)

    column_names_with_values_as_conditions = {"weather": 'sunny', "play": 'no'}
    row_indices_that_satisfy_conditions = dataframe_manager_object_00.get_rows_from_table_given_column_names_and_value_as_conditions(dataframe_object, column_names_with_values_as_conditions)
    print(row_indices_that_satisfy_conditions)
    column_names_with_values_as_sunny_and_no = len(row_indices_that_satisfy_conditions)

    sum_column_no = column_names_with_values_as_overcast_and_no + column_names_with_values_as_rainy_and_no + column_names_with_values_as_sunny_and_no
    sum_column_yes = column_names_with_values_as_overcast_and_yes + column_names_with_values_as_rainy_and_yes + column_names_with_values_as_sunny_and_yes

    column_headers, row_headers = ['weather', 'no', 'yes'], ['overcast', 'rainy', 'sunny', 'grand_total']
    # option 1: create dataframe table with array with_row_names_and_column_names in the array or matrix
    data_table_values_N_by_M_with_row_names_and_column_names = np.array(
        [column_headers,  # with row names or column names
         [row_headers[0], column_names_with_values_as_overcast_and_no, column_names_with_values_as_overcast_and_yes],
         [row_headers[1], column_names_with_values_as_rainy_and_no, column_names_with_values_as_rainy_and_yes],
         [row_headers[2], column_names_with_values_as_sunny_and_no, column_names_with_values_as_sunny_and_yes],
         [row_headers[3], sum_column_no, sum_column_yes],
         ])

    print(dataframe_manager_object_00.get_dataframe_object_name())
    dataframe_object_00 = dataframe_manager_object_00.create_dataframe_object_with_data_table_N_by_M_with_row_names_and_column_names(data_table_values_N_by_M_with_row_names_and_column_names)
    print(dataframe_object_00)

    # create another dataframe table
    dataframe_table_name = 'likelihood_table'
    id_likelihood_table = "Usage Agent: Agent <dataframe_manager>: [" + dataframe_table_name + "]"
    print("=====[" + id_likelihood_table + " Start]===== \n")
    dataframe_manager_object_01 = dataframe_manager(id_likelihood_table)
    dataframe_manager_object_01.set_dataframe_object_name(dataframe_table_name)

    total = sum_column_no + sum_column_yes
    probability_no, probability_yes = (sum_column_no / total), (sum_column_yes / total)
    probability_overcast, probability_rainy, probability_sunny = ((column_names_with_values_as_overcast_and_no + column_names_with_values_as_overcast_and_yes)/total), ((column_names_with_values_as_rainy_and_no + column_names_with_values_as_rainy_and_yes)/total), ((column_names_with_values_as_sunny_and_no + column_names_with_values_as_sunny_and_yes)/total)
    column_headers, row_headers = ['weather', 'no', 'yes', 'probabilty'], ['overcast', 'rainy', 'sunny', 'grand_total', 'probabilty']
    # option 1: create dataframe table with array with_row_names_and_column_names in the array or matrix
    data_table_values_N_by_M_with_row_names_and_column_names = np.array(
        [column_headers,  # with row names or column names
         [row_headers[0], column_names_with_values_as_overcast_and_no, column_names_with_values_as_overcast_and_yes, probability_overcast],
         [row_headers[1], column_names_with_values_as_rainy_and_no, column_names_with_values_as_rainy_and_yes, probability_rainy],
         [row_headers[2], column_names_with_values_as_sunny_and_no, column_names_with_values_as_sunny_and_yes, probability_sunny],
         [row_headers[3], sum_column_no, sum_column_yes, None],
         [row_headers[4], probability_no, probability_yes, None]
         ])

    print(dataframe_manager_object_01.get_dataframe_object_name())
    dataframe_object_01 = dataframe_manager_object_01.create_dataframe_object_with_data_table_N_by_M_with_row_names_and_column_names(data_table_values_N_by_M_with_row_names_and_column_names)
    print(dataframe_object_01)
    """
    Find out the possibility of whether there are plays in Rainy condition? Find: P(Yes|Rainy) = P(Rainy|Yes) * P(Yes) / P(Rainy)
    P(Rainy|Yes) = 2/9 = 0.222
    P(Yes) = 9/14 = 0.64
    P(Rainy) = 5/14 = 0.36
    P(Yes|Rainy) = 0.222*0.64/0.36 = 0.39
    """
    probability_Rainy_given_Yes = float(column_names_with_values_as_rainy_and_yes / sum_column_yes)
    probability_Rainy = float(sum_column_no / total)
    probability_Yes = float(sum_column_yes / total)
    print("P(Rainy | Yes) = ", probability_Rainy_given_Yes)
    print("P(Yes) = ", probability_Yes)
    print("P(Rainy) = ", probability_Rainy)
    '''
        P(outcome|evidence) =   P(Likelihood of Evidence) x Prior prob of outcome
                               ___________________________________________
                                                    P(Evidence)
    '''
    print("P(Yes | Rainy) = ", float((probability_Rainy_given_Yes * probability_Yes)/ probability_Rainy))


    # 'fruit' identification example
    file_location = '../../../Test_Usages/data/file/test_data/dataset_02.csv'

    id = "Usage Agent: Agent <dataframe_manager>"
    print("=====[" + id + " Start]===== \n")
    dataframe_manager_object_02 = dataframe_manager(id)
    dataframe_object_02 = dataframe_manager_object_02.load_data_from_csv(file_location)
    print(dataframe_object_02)
    attributes = dataframe_manager_object_02.get_column_headers(dataframe_object_02)
    print(attributes[1:(len(attributes)-1)])
    types = dataframe_manager_object_02.get_unique_values_of_fields_under_column(dataframe_object_02, 'Type')
    print(types)

    # compute Prior probabilities (as base rates)
    """
    P(Banana) = 0.5 //(500/1000) 
    P(Orange) = 0.3 
    P(Other Fruit) = 0.2
    """
    # row_name, column_name = 'Total', 'Total'
    # total = dataframe_manager_object_02.get_data_by_row_and_column_names (dataframe_object_02, row_name, column_name)
    row_index, column_index = 3, 7
    total = dataframe_manager_object_02.get_data_by_row_and_column_indices (dataframe_object_02, row_index, column_index)
    row_index, column_index = 0, 7
    banana_total = dataframe_manager_object_02.get_data_by_row_and_column_indices(dataframe_object_02, row_index, column_index)
    probability_banana = float(banana_total/total)
    print("probability_banana = ", probability_banana)
    row_index, column_index = 1, 7
    orange_total = dataframe_manager_object_02.get_data_by_row_and_column_indices(dataframe_object_02, row_index, column_index)
    probability_orange = float(orange_total/total)
    print("probability_orange = ", probability_orange)
    row_index, column_index = 2, 7
    other_fruit_total = dataframe_manager_object_02.get_data_by_row_and_column_indices(dataframe_object_02, row_index, column_index)
    probability_other_fruit = float(other_fruit_total / total)
    print("probability_orange = ", probability_other_fruit)

    """
    # compute Probability of "Evidence"
    P(Long) = 0.5 
    P(Sweet) = 0.65 
    P(Yellow) = 0.8
    # compute Probability of "Likelihood"
    P(Long|Banana) = 0.8 // 400/500
    P(Long|Orange) = 0 [Oranges are never long in all the fruit we have seen.] .... 
    P(Yellow|Other Fruit) = 50/200 = 0.25 
    P(Not Yellow|Other Fruit) = 0.75
    
    Given data on 1000 pieces of fruit ('training set' predict the type of any new fruit we encounter). They happen to be Banana, Orange or some Other Fruit. 3 characteristics about each fruit: Long, Sweet and color Yellow.
Given a Fruit, how to classify it? given the properties of an unknown fruit, and asked to classify it. We are told that the fruit is Long, Sweet and Yellow. run the numbers for each of the 3 outcomes, 1 by 1. Then choose the highest probability and 'classify' unknown fruit as belonging to the class that had the highest probability based on our prior evidence (our 1000 fruit training set):
P(Banana|Long, Sweet and Yellow) = 
P(Long|Banana) * P(Sweet|Banana) * P(Yellow|Banana) * P(banana) 
_______________________________________________________________ 
P(Long) * P(Sweet) * P(Yellow) 
= 0.8 * 0.7 * 0.9 * 0.5 / P(evidence) 
= 0.252 / P(evidence) 

P(Orange|Long, Sweet and Yellow) = 0 

P(Other Fruit|Long, Sweet and Yellow) =
P(Long|Other fruit) * P(Sweet|Other fruit) * P(Yellow|Other fruit) * P(Other Fruit) 
____________________________________________________________________________________ 
P(evidence) 

= (100/200 * 150/200 * 50/200 * 200/1000) / P(evidence) 
= 0.01875 / P(evidence)
By an overwhelming margin (0.252 >> 0.01875), classify this Sweet/Long/Yellow fruit as likely to be a Banana.

Let z = 1 / P(evidence). Compute following 3 quantities.
P(Banana|evidence) = z * Prob(Banana) * Prob(Evidence1|Banana) * Prob(Evidence2|Banana) ... 
P(Orange|Evidence) = z * Prob(Orange) * Prob(Evidence1|Orange) * Prob(Evidence2|Orange) ... 
P(Other|Evidence) = z * Prob(Other) * Prob(Evidence1|Other) * Prob(Evidence2|Other) ...
    """

