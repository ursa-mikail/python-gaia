import os, sys

# point to path
lib_path = os.path.abspath('../../data')
sys.path.append(lib_path)

# import package from path
from data_generator import data_generator	# file name


class data_sampler:
    """ Template model of Gaia """
    id = "data_sampler"
    data_generator_object = data_generator("Library Agent: Internal Agent <data_generator>")

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    # add other methods

    def select_data_random_sampling (self, number_of_data_required, data_array):
        sampled_data = []
        size_of_data_array = len(data_array)

        shuffled_indices = self.data_generator_object.generate_scrambled_indices(size_of_data_array)

        for i in range(0, number_of_data_required):
            sampled_data.append(data_array[shuffled_indices[i]])

        return sampled_data

    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = [];

        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <data_sampler>"
    print("=====[" + id + " Start]===== \n")
    data_sampler_object = data_sampler (id)
    data_sampler_object.who_am_i()

    # import _Gaia._gaia
    # help(data_sampler) # introspect

    number_of_data_required = 20
    data_array = list(range(1, 5000))
    # data_array = ['reminiscent', 'jellyfish', 'vengeful', 'fierce', 'uppity', 'aquatic', 'rural', 'scattered', 'pump', 'fact', 'unknown', 'committee', 'thumb', 'ocean', 'communicate', 'crabby', 'judicious', 'harsh', 'nervous', 'well-made', 'rare', 'ship', 'direction', 'vagabond', 'record', 'island', 'tomatoes', 'verse', 'past', 'stretch', 'polish', 'bad', 'future', 'wandering', 'raise', 'moaning', 'gorgeous', 'shock', 'delay', 'wink', 'ring', 'trashy', 'ill-fated', 'gentle', 'lying', 'increase', 'oceanic', 'carry', 'regret', 'dramatic', 'cross', 'jump', 'annoyed', 'private', 'ursa']
    sampled_data = data_sampler_object.select_data_random_sampling(number_of_data_required, data_array)
    print("data_array: ", data_array)
    print("sampled_data: ", sampled_data)

    print("=====[" + id + " End]===== \n");

"""
# version: 2018-01-20_0122hr_38sec
"""