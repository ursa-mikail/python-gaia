import collections

"""
as base support json tree and graph
"""
class dictionary_manager:
    """ Template model of Gaia """
    id = "dictionary_manager"

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    # node object
    def initialize_dictionary_object(self, number_of_entries): # entries := (key, value) pair
        node_object = []
        for i in range(0, number_of_entries):
            node_object.append(collections.defaultdict(dict))

        return node_object

    def create_dictionary_entry_object(self, node_key, node_value): # entries := (key, value) pair; fields_entry, values_entry):  # fields := keys
        node_object = collections.defaultdict(dict) # dictionary_object
        # number_of_entries = len(fields_entry) # assert len(fields_entry) == len(values_entry)
        node_object[node_key] = node_value  # create fundamental dictionary item

        return node_object

    def add_dictionary_entry_to_node_object(self, node_parent_object, node_child_object):
        node_parent_object.update(node_child_object)

        return node_parent_object

    # add node (object_list) to the parent node (node)
    def add_dictionary_object_list_to_object(self, node_parent_object, node_children_object):
        number_of_node_child_objects = len(node_children_object)

        for i in range(0, number_of_node_child_objects):
            node_parent_object.update(node_children_object[i])

        return node_parent_object

    def who_am_i(self):  #
        """ Introspection """
        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <dictionary_manager>"
    print("=====[" + id + " Start]===== \n")
    dictionary_manager_object = dictionary_manager(id)
    dictionary_manager_object.who_am_i()

    # import _Gaia._gaia
    # help(dictionary_manager) # introspect

    print("=====[" + id + " End]===== \n");

"""
# version: 2017-11-25_2350hr_20sec
"""