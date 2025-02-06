import os, os.path, time
from stat import *  # ST_SIZE etc

#
class directory_manager:
    """ Template model of Gaia """
    id = "directory_manager";
    inventory = {};
    inventory_id = "";

    operation_options = ['int_to_hex', 'hex_to_int']

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    def split_with_mutiple_delimiters (self, string, delimiters):
        """Behaves str.split but supports multiple delimiters."""

        delimiters = tuple(delimiters)
        stack = [string, ]

        for delimiter in delimiters:
            for i, substring in enumerate(stack):
                substack = substring.split(delimiter)
                stack.pop(i)
                for j, _substring in enumerate(substack):
                    stack.insert(i + j, _substring)

        return stack


    def get_directory_tree (self, root_start):
        # dir_path = '.'
        dir_path = root_start
        directory_tree = []
        depth = 0

        option = 'FILES_IN_DETAIL' # 'FILE_COUNT_ONLY'
        # is_1st_item = True
        number_of_tabs, offset = 0, 0
        offset = len(self.split_with_mutiple_delimiters(root_start, ('/', '\\'))) - 2

        # traverse root directory, and list directories as dirs and files as files
        for root, dirs, files in os.walk(dir_path):
            # path = root.split('/')
            path = self.split_with_mutiple_delimiters(root, ('/', '\\'))
            # print(path)
            depth = len(path) - 2
            number_of_tabs = depth - offset
            #line_to_print = [(number_of_tabs * '\t' + '|_' + os.path.basename(root)), ("[folder] at depth: " + str(depth))]
            #print('{:<70} {:>20}'.format(*line_to_print))
            line_to_print = (number_of_tabs * '\t' + '|_' + os.path.basename(root)) + ("\t\t\t[folder] at depth: " + str(depth))
            print(''.join(line_to_print))
            # print(root)

            if (option == 'FILE_COUNT_ONLY'):
                counter_file = 0
                number_of_tabs = len(path) - offset
                depth = depth + 1
                for file in files:
                    counter_file = counter_file + 1

                if (counter_file != 0):
                    line_to_print = (number_of_tabs * '\t' + '|_ ' + str(counter_file)) + ("\t\t\t[files] at depth: " + str(depth))
                    print(''.join(line_to_print))
                depth = depth - 1
            else:
                depth = depth + 1
                counter_file = 0
                for file in files:
                    number_of_tabs = len(path) - offset
                    # line_to_print = [(number_of_tabs * '\t' + '|_' + file), ("[file] at depth: " + str(depth))]
                    # print('{:<70} {:>20}'.format(*line_to_print))
                    line_to_print = (number_of_tabs * '\t' + '|_' + file) + ("\t\t\t[file] at depth: " + str(depth))
                    print(''.join(line_to_print))
                    counter_file = counter_file + 1

                depth = depth - 1

        """
        for filename in os.listdir(dir_path):
            # print(os.path.getmtime(os.path.join(dir_path, filename)))

        for filename in os.listdir():
            info = os.stat(filename)
            print(info.st_mtime)

        print('File     	:', __file__)

        try:
            st = os.stat(__file__)
        except IOError:
            print("failed to get information about", file)
        else:
            print("file size:", st[ST_SIZE])
            print("file modified:", time.asctime(time.localtime(st[ST_MTIME])))
        """
        return directory_tree


    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = [];

        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id)


####################################
## main
####################################
if __name__ == "__main__":
    id_directory_manager = "Library Agent: Internal Agent <directory_manager>"
    print("=====[" + id_directory_manager + " Start]===== \n")
    directory_manager_object = directory_manager(id_directory_manager)

    root_start = "C://Users/Smita/PycharmProjects/Ursa/ayahuasca/gaia/Libraries/cryptography" #
    # root_start = "C://"
    directory_manager_object.get_directory_tree (root_start)

    # import _Gaia._gaia
    # help(directory_manager) # introspect

    print("=====[" + id_directory_manager + " End]===== \n");

"""
# version: 2018-02-11_1541hr_26sec
"""

"""
Notes
-----



"""