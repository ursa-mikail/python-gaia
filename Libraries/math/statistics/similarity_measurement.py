import os, sys
import math, numpy as np

# point to path
lib_path = os.path.abspath('../../data')
sys.path.append(lib_path)

# import package from path
from data_generator import data_generator	# file name


class similarity_measurement:    # similarity measures
    """ Template model of Gaia """
    id = "compute_distances"
    data_generator_object = data_generator("Library Agent: Internal Agent <data_generator>")

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    def compute_mean_absolute_error (self, coordinates_00, coordinates_01): # coordinates := x, y
        mean_absolute_error = 0
        dimensions = len(coordinates_00) # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            mean_absolute_error = mean_absolute_error  + math.fabs(coordinates_00[i] - coordinates_01[i])

        mean_absolute_error = mean_absolute_error/dimensions

        return mean_absolute_error

    def compute_mean_squared_error (self, coordinates_00, coordinates_01):
        mean_squared_error = 0
        dimensions = len(coordinates_00)  # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            mean_squared_error = mean_squared_error + math.fabs(coordinates_00[i] - coordinates_01[i]) ** 2

        mean_squared_error = mean_squared_error / dimensions

        return mean_squared_error

    def compute_root_mean_squared_error (self, coordinates_00, coordinates_01):
        mean_squared_error = self.compute_mean_squared_error(coordinates_00, coordinates_01)
        root_mean_squared_error = math.sqrt(mean_squared_error)

        return root_mean_squared_error

    # || X-Y ||_2 (L2 norm)
    # Nearest neighbor classification uses euclidean_distance; the dimensions is the number of features
    def compute_euclidean_distance (self, coordinates_00, coordinates_01): # coordinates := x, y
        euclidean_distance = 0
        dimensions = len(coordinates_00) # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            euclidean_distance = euclidean_distance + (coordinates_00[i] - coordinates_01[i])**2

        euclidean_distance = math.sqrt(euclidean_distance)

        return euclidean_distance

    # || X-Y ||_1 (L1 norm)
    def compute_manhattan_distance (self, coordinates_00, coordinates_01): # coordinates := x, y
        manhattan_distance = 0
        dimensions = len(coordinates_00) # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            manhattan_distance = manhattan_distance + math.fabs(coordinates_00[i] - coordinates_01[i])

        return manhattan_distance
    """
    When p=1, the distance is known as the Manhattan distance.
    When p=2, the distance is known as the Euclidean distance.
    In the limit that p --> +infinity, the distance is known as the Chebyshev distance.
    """
    def compute_minkowski_distance (self, coordinates_00, coordinates_01): # coordinates := x, y
        minkowski_distance = 0
        dimensions = len(coordinates_00) # assert all dimensions of all coordinates are the same
        p = dimensions

        for i in range(0, dimensions):
            minkowski_distance = minkowski_distance + math.fabs(coordinates_00[i] - coordinates_01[i])**p

        minkowski_distance = minkowski_distance**(1/p)

        return minkowski_distance

    def compute_canberra_distance(self, coordinates_00, coordinates_01):  # coordinates := x, y
        canberra_distance = 0
        dimensions = len(coordinates_00)  # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            numerator = math.fabs(coordinates_00[i] - coordinates_01[i])
            denominator = math.fabs(coordinates_00[i]) + math.fabs(coordinates_01[i])
            canberra_distance = canberra_distance + (numerator / denominator)

        return canberra_distance

    def compute_chebyshev_distance(self, coordinates_00, coordinates_01):  # coordinates := x, y
        chebyshev_distances = []
        dimensions = len(coordinates_00)  # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            chebyshev_distances.append(math.fabs(coordinates_00[i] - coordinates_01[i]))

        chebyshev_distance_max = max(chebyshev_distances)

        return chebyshev_distance_max

    def compute_bray_curtis_distance(self, coordinates_00, coordinates_01):  # coordinates := x, y
        numerator, denominator = 0, 0

        bray_curtis_distance = 0
        dimensions = len(coordinates_00)  # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            numerator = numerator + math.fabs(coordinates_00[i] - coordinates_01[i])
            denominator = denominator + (coordinates_00[i] + coordinates_01[i])

        bray_curtis_distance = numerator/denominator

        return bray_curtis_distance

    def compute_angular_separation(self, coordinates_00, coordinates_01):  # coordinates := x, y
        numerator, denominator = 0, 0
        denominator_00, denominator_01 = 0, 0

        angular_separation = 0
        dimensions = len(coordinates_00)  # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            numerator = numerator + (coordinates_00[i] * coordinates_01[i])
            denominator_00 = denominator_00 + (coordinates_00[i]**2)
            denominator_01 = denominator_01 + (coordinates_01[i]**2)

        denominator = denominator_00 * denominator_01

        if (denominator == 0):
            return 0
        else:
            angular_separation = numerator/math.sqrt(denominator)

        return angular_separation

    def square_rooted(self, x):
        return round(math.sqrt(sum([a * a for a in x])), 3)

    def compute_cosine_similarity(self, coordinates_00, coordinates_01):
        numerator = sum(a*b for a, b in zip(coordinates_00, coordinates_01))
        denominator = self.square_rooted(coordinates_00) * self.square_rooted(coordinates_01)
        return round(numerator / float(denominator), 3)

    def compute_jaccard_similarity(self, x, y):
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality / float(union_cardinality)

    # pearson_correlation_coefficient
    def compute_correlation_coefficient(self, coordinates_00, coordinates_01):  # coordinates := x, y
        coordinates_00_mean = np.mean(coordinates_00)
        coordinates_01_mean = np.mean(coordinates_01)
        numerator = 0
        denominator_00, denominator_01 = 0, 0

        correlation_coefficient = 0
        dimensions = len(coordinates_00)  # assert all dimensions of all coordinates are the same

        for i in range(0, dimensions):
            numerator = numerator + ((coordinates_00[i] - coordinates_00_mean)*(coordinates_01[i] - coordinates_01_mean))
            denominator_00 = denominator_00 + (coordinates_00[i] - coordinates_00_mean)**2
            denominator_01 = denominator_01 + (coordinates_01[i] - coordinates_01_mean)**2

        denominator = math.sqrt(denominator_00*denominator_01)

        if (denominator == 0):
            return 0
        else:
            correlation_coefficient = numerator/denominator

        return correlation_coefficient

    def normalize_data_with_mean_0_and_variance_1 (self, data):
        data_normalized = []

        for i in range(0, len(data)):
            data_normalized.append((data[i] - np.mean(data)) / np.std(data))

        return data_normalized

    def normalize_data_in_range_0_to_1 (self, data):
        data_normalized = []
        data_max, data_min = max(data), min(data)

        for i in range(0, len(data)):
            data_normalized.append((data_max - data[i]) / (data_max - data_min))

        return data_normalized

    def compute_data_energy (self, data):   # sum(|x_n|^2) == sum(|X_f|^2)/N , Parseval's theorem
        data_energy = 0

        for i in range(0, len(data)):
            data_energy = data_energy + (math.fabs(data[i]))**2

        return data_energy

    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = []

        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <similarity_measurement>"
    print("=====[" + id + " Start]===== \n")
    similarity_measurement_object = similarity_measurement (id)
    similarity_measurement_object.who_am_i()

    # import _Gaia._gaia
    # help(similarity_measurement) # introspect

    coordinates_00 = [0, 3, 4, 5] # 4-d
    coordinates_01 = [7, 6, 3, -1]
    euclidean_distance = similarity_measurement_object.compute_euclidean_distance(coordinates_00, coordinates_01)
    print("euclidean_distance: ", euclidean_distance)
    manhattan_distance = similarity_measurement_object.compute_manhattan_distance(coordinates_00, coordinates_01)
    print("manhattan_distance: ", manhattan_distance)

    coordinates_00 = [ 2, 4, 5, 3, 8, 2 ]
    coordinates_01 = [ 3, 1, 5, -3, 7, 2]
    coordinates_00, coordinates_01 = [0, 3, 4, 5], [7, 6, 3, -1]
    minkowski_distance = similarity_measurement_object.compute_minkowski_distance(coordinates_00, coordinates_01)
    print("minkowski_distance: ", minkowski_distance)

    coordinates_00, coordinates_01 = [3, 45, 7, 2],  [2, 54, 13, 15]
    cosine_similarity = similarity_measurement_object.compute_cosine_similarity(coordinates_00, coordinates_01)
    print("cosine_similarity: ", cosine_similarity)
    coordinates_00, coordinates_01 = [0, 1, 2, 5, 6], [0, 2, 3, 5, 7, 9]
    jaccard_similarity = similarity_measurement_object.compute_jaccard_similarity(coordinates_00, coordinates_01)
    print("jaccard_similarity: ", jaccard_similarity)
    coordinates_00, coordinates_01 = [0, 3, 4, 5], [7, 6, 3, -1]
    canberra_distance = similarity_measurement_object.compute_canberra_distance(coordinates_00, coordinates_01)
    print("canberra_distance: ", canberra_distance)
    chebyshev_distance = similarity_measurement_object.compute_chebyshev_distance(coordinates_00, coordinates_01)
    print("chebyshev_distance: ", chebyshev_distance)
    correlation_coefficient = similarity_measurement_object.compute_correlation_coefficient(coordinates_00, coordinates_01)
    print("correlation_coefficient: ", correlation_coefficient)

    bray_curtis_distance = similarity_measurement_object.compute_bray_curtis_distance(coordinates_00, coordinates_01)
    print("bray_curtis_distance: ", bray_curtis_distance)

    angular_separation = similarity_measurement_object.compute_angular_separation(coordinates_00, coordinates_01)
    print("angular_separation: ", angular_separation)

    coordinates_00_normalized = similarity_measurement_object.normalize_data_with_mean_0_and_variance_1(coordinates_00)
    print("coordinates_00: ", coordinates_00)
    print("coordinates_00_normalized (with_mean_0_and_variance_1): ", coordinates_00_normalized)

    coordinates_00_normalized = similarity_measurement_object.normalize_data_in_range_0_to_1(coordinates_00)
    print("coordinates_00: ", coordinates_00)
    print("coordinates_00_normalized (in_range_0_to_1): ", coordinates_00_normalized)

    range_lower, range_upper, number_of_data_elements, bin = 0, 1, 100, 0.1
    # data = [50,30,20,35,25]
    data = np.linspace(range_lower, range_upper, number_of_data_elements)
    data = np.arange(range_lower, (range_upper + bin), bin)
    print("data: ", data, " (#(data): ", len(data), " )")
    SNR = np.mean(data)/np.std(data)
    print("SNR: ", SNR)

    # import _Gaia._gaia
    # help(similarity_measurement) # introspect

    print("=====[" + id + " End]===== \n");

"""
s_ij = 1 - d_ij  # similarity = 1 - dissimilarity , given they are normalized

from decimal import Decimal


def nth_root(value, n_root):
    root_value = 1 / float(n_root)
    return round(Decimal(value) ** Decimal(root_value), 3)


def check_minkowski_distance(x, y, p_value):
    return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)

print (check_minkowski_distance(coordinates_00, coordinates_01, 4))

ref: 
http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
http://people.revoledu.com/kardi/
"""
"""
# version: 2018-01-20_0529hr_38sec
"""