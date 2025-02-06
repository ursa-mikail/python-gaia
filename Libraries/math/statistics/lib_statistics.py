import numpy as np
import math

import os, sys

# point to path
lib_path = os.path.abspath('../../data/')
sys.path.append(lib_path)

from data_processor import data_processor

class lib_statistics:
    """ Template model of Gaia """
    id = "lib_statistics";
    inventory = {};
    inventory_id = "";

    id_data_processor = "Library Agent <data_processor>"
    print("=====[" + id_data_processor + " Start]===== \n")
    data_processor_object = data_processor(id_data_processor)

    operation_options = ['mean', 'median', 'standard_deviation', 'variance']

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id);

    def operation_on_array_or_matrix (self, array_or_matrix, operation_chosen):
        if (operation_chosen == self.operation_options[0]):
            martix_resultant = np.mean(array_or_matrix)
        if (operation_chosen == self.operation_options[1]):
            martix_resultant = np.median(array_or_matrix)
        if (operation_chosen == self.operation_options[2]):
            martix_resultant = np.std(array_or_matrix) # Standard deviation:= square root of average of squared deviations from mean. standard deviation, std = sqrt(mean(abs(x - x.mean())**2))
        if (operation_chosen == self.operation_options[3]):
            martix_resultant = np.var(array_or_matrix) # variance = average of squared deviations, i.e., mean(abs(x - x.mean())**2). i.e., standard deviation = square root of variance.

        return martix_resultant

    def compute_covariance(self, x, y):
        x_bar = np.mean(x)
        y_bar = np.mean(y)
        covariance_result = 0

        number_of_elements = len(x)  # assert (len(x) == len(y))
        for i in range(0, number_of_elements):
            covariance_result = covariance_result + (x[i] - x_bar) * (y[i] - y_bar)

        covariance_result = covariance_result / (number_of_elements - 1)

        return covariance_result

    def compute_correlation(self, x, y):
        covariance_result = self.compute_covariance(x, y)
        x_bar = np.mean(x)
        y_bar = np.mean(y)

        number_of_elements = len(x)  # assert (len(x) == len(y))
        s_x = 0  # np.std(x) # sample standard deviation of random variable x
        s_y = 0  # np.std(y) # sample standard deviation of random variable y

        for i in range(0, number_of_elements):
            s_x = s_x + (x[i] - x_bar) ** 2 / (number_of_elements - 1)
            s_y = s_y + (y[i] - y_bar) ** 2 / (number_of_elements - 1)

        s_x = math.sqrt(s_x)
        s_y = math.sqrt(s_y)

        # print("s_x = ", s_x)
        # print("s_y = ", s_y)

        correlation_result = covariance_result / (s_x * s_y)

        return correlation_result

    def compute_covariance_matrix (self, variables_lists):
        number_of_variables = len(variables_lists)
        # number_of_observations = len(variables_lists[0])  # assert all len(variables_lists) are equal
        x_bar = []

        # compute all mean
        for i in range(0, number_of_variables):
            x_bar.append(np.mean(variables_lists[i]))

        row_size, column_size = number_of_variables, number_of_variables
        S = [[0 for x in range(row_size)] for y in range(column_size)]  # variance-covariance matrix (initialization)

        for i in range(0, row_size):
            for j in range(0, column_size):
                S[i][j] = self.compute_covariance(variables_lists[i], variables_lists[j])

        covariance_matrix = S
        # mean vector is referred to as the centroid
        # variance-covariance matrix as the dispersion or dispersion matrix.
        # variance-covariance matrix and covariance matrix are used interchangeably.

        return covariance_matrix

    def compute_histogram(self, x_data): # PDF
        frequencies, bins = np.histogram(x_data)

        return frequencies, bins

    def compute_CDF(self, x_data):
        cumulative_data = np.cumsum(x_data)

        return cumulative_data

    def compute_chi_square_statistic(self, observed_data):
        mean_value = np.mean(observed_data)
        residual_data = self.data_processor_object.arithmetic_operation_element_wise_between_2_arrays_or_matrices(observed_data,
                                                                                             [mean_value] * len(
                                                                                                 observed_data),
                                                                                             "subtract")

        components = self.data_processor_object.arithmetic_operation_element_wise_between_2_arrays_or_matrices(residual_data**2,
                                                                                                  [mean_value] * len(
                                                                                                      observed_data),
                                                                                                  "divide")

        chi_square_statistic = np.sum(components)

        return chi_square_statistic

    def compute_chi_square_statistic_given_population_data (self, observed_data, data_population):
        data_population_ratios = data_population / sum(data_population)  # Get population ratios
        expected_value = data_population_ratios * sum(observed_data)  # Get expected counts
        residual_data = self.data_processor_object.arithmetic_operation_element_wise_between_2_arrays_or_matrices(observed_data,
                                                                                                                  expected_value,
                                                                                                                    "subtract")


        components = self.data_processor_object.arithmetic_operation_element_wise_between_2_arrays_or_matrices(residual_data**2,
                                                                                                  expected_value,
                                                                                                  "divide")

        chi_square_statistic = np.sum(components)

        return chi_square_statistic

    def compute_entropy(self, probability_list): #
        number_of_elements = len(probability_list)
        base = 2
        entropy = 0

        for i in range(0, number_of_elements):
            if (probability_list[i] == 0): # Define: −0*log2(0) = 0
                pass
            else:
                entropy = entropy + (probability_list[i] * math.log(probability_list[i], base))

        entropy = -1 * entropy

        return entropy

    def compute_log_odds (self, probability): # likelihood
        if (probability != 0):
            log_odds = math.log((probability/(1 - probability)))
        else:
            print("Error: probability is zero")
            log_odds = None

        return log_odds

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
    id = "Library Agent: Internal Agent <lib_statistics>"
    print ("=====[" + id + " Start]===== \n")
    lib_statistics_object = lib_statistics(id)
    lib_statistics_object.who_am_i()



    #import _Gaia._gaia
    #help(lib_statistics) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-09-23_2010hr_04sec
"""		