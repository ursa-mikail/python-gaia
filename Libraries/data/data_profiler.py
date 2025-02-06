import numpy as np

class data_profiler:
    """ Template model of Gaia """
    id = "data_profiler"

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    def if_data_exist (self, data_target, data):  #
        exist_status = data_target in data

        return exist_status

    def determine_positions_of_data_target (self, data_target, data):  #
        positions = [i for i, x in enumerate(data) if x == data_target]

        return positions

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
    id = "Library Agent: Internal Agent <data_profiler>"
    print("=====[" + id + " Start]===== \n")
    data_profiler_object = data_profiler(id)
    data_profiler_object.who_am_i()

    # import _Gaia._gaia
    # help(data_profiler) # introspect

    range_lower, range_upper, number_of_data_elements, bin = 11, 100, 100, 0.5 # 0.1
    data = np.arange(range_lower, (range_upper + bin), bin)
    data = list(data)
    print("data: ", data, " (#(data): ", len(data), " )")

    data_target = 11.5
    data[12] = data_target

    if (data_profiler_object.if_data_exist(data_target, data)):
        positions = data_profiler_object.determine_positions_of_data_target(data_target, data)
        print("data_target: ", data_target, " exists at ", positions)
        print("occurences: ", len(positions))
    else:
        print("data_target: ", data_target, " absent")


    print("=====[" + id + " End]===== \n");

"""
# version: 2018-01-20_1637hr_30sec
"""