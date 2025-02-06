import os, sys

# point to path
lib_path = os.path.abspath('../../text')
sys.path.append(lib_path)

# import package from path
from string_processor import string_processor_class	# file name
from text_processor import text_processor	# file name

import json

class json_manager:
    """ Template model of Gaia """
    id = "json_manager";

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)

    def load_json_data_from_file (self, json_file):
        data_json = json.load(open(json_file))

        return data_json

    def check_json_format(self, files_json_with_path):
        json_files_valid, json_files_invalid = [], []

        for files in files_json_with_path:  # os.listdir(os.getcwd()):
            with open(files) as json_file:
                try:
                    json.load(json_file)
                    json_files_valid.append(files)
                except ValueError as e:
                    print(("JSON object issue: %s") % e)
                    json_files_invalid.append(files)
        print(json_files_invalid, len(json_files_valid))
        return json_files_valid, json_files_invalid

    #
    def check_json_format_with_json_stream(self, json_stream):
        try:
            print("Valid JSON format")
            return json.loads(json_stream)
        except ValueError as e:  # except InvalidDataException:
            print('invalid json: %s' % e)
            return None  # or: raise

    def check_json_format_with_json_file(self, file_json_with_path):
        try:
            with open(file_json_with_path) as f:
                print("Valid JSON format")
                return json.load(f)
        except ValueError as e:  # except InvalidDataException:
            print('invalid json: %s' % e)
            return None  # or: raise

    def write_json_data_to_file (self, json_file_data, json_file):
        with open(json_file, 'w') as json_file_out:
            json.dump(json_file_data, json_file_out, indent=4)

        json_file_out.close()

        return None

    def get_depth(self, x):
        if type(x) is dict and x:
            return 1 + max(self.get_depth(x[a]) for a in x)
        if type(x) is list and x:
            return 1 + max(self.get_depth(a) for a in x)
        return 0

    def get_max_depth_of_json_file_structure(self, contents_serialized_json):
        length_of_contents = len(contents_serialized_json)

        max_depth = 0;

        brace_start, brace_end = '{', '}'
        layer_count = -1  # layer_number_index is depth, starting from root which is 0

        for i in range(0, length_of_contents):
            if (contents_serialized_json[i] == brace_start):
                layer_count = layer_count + 1
                if (layer_count > max_depth):
                    max_depth = layer_count

            if (contents_serialized_json[i] == brace_end):
                layer_count = layer_count - 1

        return max_depth

    def extract_json_content_at_N_layer(self, contents_serialized_json, layer_number_index):
        length_of_contents = len(contents_serialized_json)

        content_extracted = []

        brace_start = '{'
        brace_end = '}'
        layer_count = -1  # layer_number_index is depth, starting from root which is 0

        for i in range(0, length_of_contents):
            if (contents_serialized_json[i] == brace_start):
                layer_count = layer_count + 1

            # starts recording
            if (layer_count == layer_number_index):
                content_extracted.append(contents_serialized_json[i])
            else:
                pass

            if (contents_serialized_json[i] == brace_end):
                layer_count = layer_count - 1

        # list to string
        content_extracted = ''.join(content_extracted)
        return content_extracted

    def extract_json_content_under_N_layer(self, contents_serialized_json, layer_number_index):
        length_of_contents = len(contents_serialized_json)

        content_extracted = []

        brace_start, brace_end = '{', '}'
        layer_count = -1  # layer_number_index is depth, starting from root which is 0

        for i in range(0, length_of_contents):
            if (contents_serialized_json[i] == brace_start):
                layer_count = layer_count + 1

            # starts recording
            if (layer_count >= layer_number_index):
                content_extracted.append(contents_serialized_json[i])
            else:
                pass

            if (contents_serialized_json[i] == brace_end):
                layer_count = layer_count - 1

        content_extracted = ''.join(content_extracted)
        return content_extracted

    def search_for_position_of_end_brace_to_skip_section (self, contents_serialized_json, current_position):
        position_after_end_brace_of_section = 0
        length_of_contents = len(contents_serialized_json)
        brace_start, brace_end = '{', '}'
        number_of_brace_to_close = 1

        i = current_position + 1 # skip brace_start
        #print(contents_serialized_json)
        #print(type(contents_serialized_json))
        #print(length_of_contents)

        while i < length_of_contents:
            # print(contents_serialized_json[i])

            if (contents_serialized_json[i] == brace_end):
                number_of_brace_to_close = number_of_brace_to_close - 1
            if (contents_serialized_json[i] == brace_start):
                number_of_brace_to_close = number_of_brace_to_close + 1

            if (number_of_brace_to_close == 0): # end of section found
                position_after_end_brace_of_section = i + 1
                break
             

            i = i + 1 # while loop counter
        return position_after_end_brace_of_section

    def extract_subsection(self, contents_serialized_json, index_of_brace_start):
        subsection = ""

        length_of_contents = len(contents_serialized_json)
        brace_start, brace_end = '{', '}'

        i = index_of_brace_start

        while i < length_of_contents:
            # print(contents_serialized_json[i])

            if (contents_serialized_json[i] != brace_end):
                subsection = subsection + (contents_serialized_json[i])
            else:
                subsection = subsection + (contents_serialized_json[i])
                break

            i = i + 1  # while loop counter

        return subsection

# Uter-construction
    def extract_json_content_under_index (self, contents_serialized_json, index):
        length_of_contents = len(contents_serialized_json)

        index_directors = index.split('.')
        number_of_depeth_to_search = len(index_directors)
        index_directors_int = []
        current_depth = 0   # depth starts from 0, which is the equivalent of depth index 1

        for i in range(0, len(index_directors)):
            index_directors_int.append(int(index_directors[i]))

        # print(index_directors_int)

        index_of_current_section = 1
        search_of_index_within_depth_counter = 0
        index_of_current_section_director = index_directors_int[search_of_index_within_depth_counter]
        content_extracted = []

        brace_start, brace_end = '{', '}'
        layer_count = -1  # layer_number_index is depth, starting from root which is 0

        while i < length_of_contents:
            if (contents_serialized_json[i] == brace_start):
                layer_count = layer_count + 1

            if (index_of_current_section != index_of_current_section_director):
                # skip this section, don't search this section
                i = self.search_for_position_of_end_brace_to_skip_section (contents_serialized_json, i) # takes current_position, finds position_after_end_brace_of_section
                i = i - 1 # point back to the position of brace_end, let the loop check if the next may be a brace_start
                layer_count = layer_count - 1 # since it left the brace_start
                index_of_current_section = index_of_current_section + 1  # go to next section
            else:
                # chose this section and search for next subsection layer
                search_of_index_within_depth_counter = search_of_index_within_depth_counter + 1
                if (search_of_index_within_depth_counter < len(index_directors_int)):
                    print(index_of_current_section_director)
                    index_of_current_section_director = index_directors_int[search_of_index_within_depth_counter]
                    print(index_of_current_section_director)
                    # [last stop]
                else:
                    # if end of index_directors_int reached, start extracting
                    # print(index_directors_int[search_of_index_within_depth_counter])
                    pass; # to-do
                    # content_extracted = self.extract_subsection(contents_serialized_json, i - 1) # (i-1) point to brace_start
                    break

            i = i + 1 # while loop counter

        """
        for i in range(0, length_of_contents):
            if (contents_serialized_json[i] == brace_start):
                layer_count = layer_count + 1

            # starts recording
            if (layer_count >= layer_number_index):
                content_extracted.append(contents_serialized_json[i])
            else:
                pass

            if (contents_serialized_json[i] == brace_end):
                layer_count = layer_count - 1

        content_extracted = ''.join(content_extracted)
        
        """
        return content_extracted


    def level_exist(self, contents_serialized_json, layer_number_index): # contents_serialized_json can also be indented form
        FLAG_EXIST = False

        contents_at_layer_N = self.extract_json_content_at_N_layer(contents_serialized_json, layer_number_index)

        if (len(contents_at_layer_N) != 0):
            FLAG_EXIST = True

        return FLAG_EXIST

    def count_number_of_keys_in_json_stream(self, contents_serialized_string):
        contents_serialized_string_tokenized = contents_serialized_string.split(':')
        number_of_keys = len(contents_serialized_string_tokenized)

        return number_of_keys

    def get_keys_only_in_json_stream(self, contents_serialized_string):
        print("< Incomplete function module >: ", self.get_keys_only_in_json_stream.__name__, "[ under construction]")

        id = "Agent within get_keys_only_in_json_stream"
        string_processor_object = string_processor_class(id)
        text_processor_object = text_processor(id)

        contents_serialized_string_tokenized = contents_serialized_string.split(':')
        number_of_keys = len(contents_serialized_string_tokenized) - 1  # exclude the last segment containing values
        last_segment = contents_serialized_string_tokenized[number_of_keys]
        print("last_segment: ", last_segment)

        keys_in_contents_serialized_string = []
        values_in_contents_serialized_string = []

        for i in range(0, number_of_keys):
            #tag_string = '\n'
            symbols = ['"', ' ', "'", '\n', '{', '}', '[', ']', ',']
            string_target = contents_serialized_string_tokenized[i]
            string_target = string_processor_object.rstrip_ensure_no_symbol(symbols, string_target)
            #string_target = string_processor_object.rstrip_ensure_no_symbol(symbols, string_target)
            string_target = string_processor_object.lstrip_ensure_no_symbol(symbols, string_target)
            #string_target = string_processor_object.lstrip_ensure_no_symbol(symbols, string_target)

            string_target = string_target.split('"')

            for j in range(0, len(string_target)-1):    # omit last term which is key
                string_target_for_value = string_target[j]
                string_target_for_value = string_processor_object.rstrip_ensure_no_symbol(symbols, string_target_for_value)

                if (len(string_target_for_value) != 0):
                    values_in_contents_serialized_string.append(string_target_for_value)
                else:
                    print("No value ...")


            string_target = string_target[len(string_target)-1]

            print("string_target: ", string_target)
            #string_target = string_processor_object.lstrip_ensure_no_symbol(symbols, string_target)
            #string_target = text_processor_object.truncate_string_that_appears_before_tag(string_target, tag_string)
            keys_in_contents_serialized_string.append(string_target)

        # add back the last segment containing values
        # string_target_for_value = last_segment

        string_target = last_segment.split('"')

        for j in range(0, len(string_target) - 1):  # omit last term which is key
            string_target_for_value = string_target[j]
            string_target_for_value = string_processor_object.rstrip_ensure_no_symbol(symbols, string_target_for_value)

            if (len(string_target_for_value) != 0):
                values_in_contents_serialized_string.append(string_target_for_value)
            else:
                print("No value ...")

        return keys_in_contents_serialized_string, values_in_contents_serialized_string



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
    id = "Library Agent: Internal Agent <json_manager>"
    print("=====[" + id + " Start]===== \n")
    json_manager_object = json_manager(id)
    json_manager_object.who_am_i()

    # import _Gaia._gaia
    # help(json_manager) # introspect

    print("=====[" + id + " End]===== \n");

"""
# version: 2017-11-25_2350hr_20sec
"""