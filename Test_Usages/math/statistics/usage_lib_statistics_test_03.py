from usage_lib_statistics_support import *

def test_03 (lib_statistics_object):

    #probability_list = [5/14, 9/14] # [0.7, 0.3]
    #entropy = lib_statistics_object.compute_entropy(probability_list)

    probability_list_parent = [14/30, 16/30]
    entropy_parent = lib_statistics_object.compute_entropy(probability_list_parent)
    print("entropy_parent: ", entropy_parent)

    probability_list_child_00 = [13 / 17, 4 / 17]
    entropy_child_00 = lib_statistics_object.compute_entropy(probability_list_child_00)
    print("entropy_child_00: ", entropy_child_00)

    probability_list_child_01 = [1 / 13, 12 / 13]
    entropy_child_01 = lib_statistics_object.compute_entropy(probability_list_child_01)
    print("entropy_child_01: ", entropy_child_01)

    weighted_average_entropy_of_children = (17/30 * entropy_child_00) + (13/30*entropy_child_01)

    information_gain = entropy_parent - weighted_average_entropy_of_children
    print("information_gain:", information_gain)

    probability_list = [0.5, 0.9, 0.999, 0.01, 0.001, 0]

    for probability in probability_list:
        likelihood = lib_statistics_object.compute_log_odds(probability)
        print("likelihood: ", likelihood)

    entropy_child_01 = lib_statistics_object.compute_entropy(probability_list)
    print("entropy_child_01: ", entropy_child_01)

    probability_list_child_00 = [3/5, 2/5]
    entropy_child_00 = lib_statistics_object.compute_entropy(probability_list_child_00)
    print("entropy_child_00: ", entropy_child_00)
    probability_list_child_01 = [3/5, 2/5]
    entropy_child_01 = lib_statistics_object.compute_entropy(probability_list_child_01)
    print("entropy_child_01: ", entropy_child_01)
    probability_list_child_02 = [0/4, 1]
    entropy_child_02 = lib_statistics_object.compute_entropy(probability_list_child_02)
    print("entropy_child_02: ", entropy_child_02)

    gain = (entropy_child_00 + entropy_child_01 + entropy_child_02) - 1.577
    print("gain: ", gain)

    return None
