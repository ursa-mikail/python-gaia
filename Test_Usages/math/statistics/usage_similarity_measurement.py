####################################
import os, sys
import numpy as np
import math

# point to path
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/math/statistics')
sys.path.append(lib_path)

# import package from path
from similarity_measurement import similarity_measurement  # file name

# add other methods
def threshold_scoring(threshold, scores):
    rating = [0] * len(scores)
    for i in range(0, len(scores)):
        if (scores[i] >= threshold):
            rating[i] = 1

    return rating

def compute_guassian_factor(x, mu, sigma):
    exponent = math.exp(-(1 / 2) * (((x - mu) / sigma) ** 2))
    result = 1/(sigma*math.sqrt(2*math.pi)) * exponent

    return result

####################################
## main
####################################
if __name__ == "__main__":
    id_similarity_measurement = "Usage Agent: similarity_measurement"
    print("=====[" + id_similarity_measurement + " Start]===== \n")
    similarity_measurement_object = similarity_measurement(id_similarity_measurement)
    similarity_measurement_object.who_am_i()

    # Nearest-neighbor
    a_cards_n_reponse, b_cards_n_reponse, c_cards_n_reponse, d_cards_n_reponse, e_cards_n_reponse, f_cards_n_reponse = [2, '?'], [3, 'yes'], [2, 'no'], [1, 'no'], [1, 'no'], [4, 'yes']
    a, b, c, d, e, f = [37, 50, 2], [35, 35, 3], [22, 50, 2], [63, 200, 1], [59, 170, 1], [25, 40, 4]
    entities = [a, b, c, d, e, f]
    entities_total = len(entities)
    print("entities_total: ", entities_total)
    similarity_weights = []

    distances = []
    # Caveat: the target to be compared with is placed in the 1st position
    for i in range(1, entities_total): # start from 1 to avoid itself
        distances.append(similarity_measurement_object.compute_euclidean_distance(entities[0], entities[i]))
        # similarity_weights.append(similarity_measurement_object.compute_correlation_coefficient(entities[0], entities[i]))

    nearest_neighbor = min(distances)
    nearest_neighbor = nearest_neighbor
    nearest_neighbor_index = distances.index(nearest_neighbor) # which index
    nearest_neighbor_index = nearest_neighbor_index + 1  # as the 1st one, itself is omitted
    print("nearest_neighbor: ", nearest_neighbor, ", (nearest_neighbor_index: ", nearest_neighbor_index, " )")
    print("distances: ", distances)
    distances_sorted = sorted(distances)
    print("distances_sorted: ", distances_sorted)

    weights_total = 0
    for i in range(0, len(distances)):
        similarity_weights.append(1/(distances_sorted[i]**2))
        weights_total = weights_total + similarity_weights[i]

    #weights_total = 0.004444 +  0.004348 + 0.000043 + 0.000067 + 0.004032
    #print(0.344 + 0.336 + 0.312 + 0.005 + 0.003)
    print("similarity_weights: ", similarity_weights)

    contribution = []

    for i in range(0, len(distances)):
        contribution.append(similarity_weights[i]/weights_total)

    print("contribution: ", contribution)

    ratings = threshold_scoring(20, distances_sorted)
    print("ratings: ", ratings)

    guassian_factors = [0] * len(distances_sorted)
    guassian_factors_normalized = [0] * len(distances_sorted)

    mu, sigma = np.mean(distances_sorted), np.std(distances_sorted)

    for i in range(0, len(distances_sorted)):
        guassian_factors[i] = compute_guassian_factor(distances_sorted[i], mu, sigma)

    for i in range(0, len(distances_sorted)):
        guassian_factors_normalized[i] = guassian_factors[i]/sum(guassian_factors)

    print("guassian_factors:", guassian_factors)
    print("guassian_factors_normalized:", guassian_factors_normalized)
    print("guassian_factors_normalized_total:", sum(guassian_factors_normalized))

    print("=====[" + id_similarity_measurement + " End]===== \n");

"""
# version: 2018-01-22_1736hr_04sec
"""