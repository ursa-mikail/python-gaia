import numpy as np

from usage_lib_statistics_support import *

def test_00 (data_manipulator_object, lib_statistics_object, display_console_object):
    zeroized_flag = False
    N, M, data_type = 5, 8, 'float'  # 'int'
    matrix_NxM_00 = data_manipulator_object.create_matrix_NxM(N, M, data_type, zeroized_flag)
    print("matrix_NxM_00:\n" + str(matrix_NxM_00))

    # axis-0: row-wise; axis-1: column-wise;
    action_choices = ['mean', 'median', 'standard_deviation', 'variance']
    action_chosen = action_choices[len(action_choices) - 1]

    martix_resultant = lib_statistics_object.operation_on_array_or_matrix(matrix_NxM_00, action_chosen)
    print("Operation: " + action_chosen)
    print(martix_resultant)

    covariance = np.cov(x, y)
    print("covariance = ", covariance)
    covariance = lib_statistics_object.compute_covariance(x, y)
    print("covariance = ", covariance)
    correlation = lib_statistics_object.compute_correlation(x, y)
    print("correlation = ", correlation)

    variables_lists = [v1, v2, v3]
    S = lib_statistics_object.compute_covariance_matrix(variables_lists)
    display_console_object.display_matrix("S (aka covariance_matrix)", S)

    return None