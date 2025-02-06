import re

#
class regex_lib:
    """ Template model of Gaia """
    id = "regex_lib"

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id)


    # def find_string_given_subformat: return string token and positions (start, end)

    def check_match_exists(self):
        match_exists_status = False

        # to be directed to a match operation
        # match = re.search(r'(\w+), (\w+): (\S+)', contactInfo) # match operation

        if match:
            match_exists_status = True
        else:
            match_exists_status = False

        return match_exists_status

    def parse_regex_strict_formatted_command(self, regex_formatted_command_list):
        # To avoid confusion while dealing with regex, use Raw Strings as r'expression'.
        # usage: regex_formatted_command_list: number: \d; alphabet: \w;
        """
        :param regex_formatted_command_list:
        :return:

        + := >=1 occurrences of the pattern to its left, e.g. 'i+' = one or more i's
        * := >= 0 occurrences of the pattern to its left
        ? := match 0 or 1 occurrences of the pattern to its left
        ref: https://developers.google.com/edu/python/regular-expressions

        e.g. r'[\w.-]+\@[\w.-]+.com'  matches ## 'ursa-major@ei.com'
        """
        regex_formatted_command_list = 0
        contains_numbers, contains_alphabets_ignore_case, contains_ascii_symbols, contains_any = '(\d+)', '([a-zA-Z]+)', '([^\w]+)', '(.*)'
        is_number, is_alphabet_ignore_case, is_ascii_symbol, is_any = '(\d)', '([a-zA-Z])', '([^\w])', '(.)'

        # exactly N {N}, >= N {N,}, e.g. \d{N,}

        contains_alphabets_upper_case, contains_alphabets_lower_case = '([A-Z]+)', '([a-z]+)'
        is_alphabets_upper_case, is_alphabets_lower_case = '([A-Z])', '([a-z])'

        return None

    def get_matched_substrings_found_and_locations(self, regex, target_string):
        matched_substrings = regex.findall(target_string)

        iterator = regex.finditer(target_string)

        locations = []
        for match in iterator:
            locations.append(match.span()) # [(start_index_i, (end_index_i + 1))]

        return [matched_substrings, locations]

    def filter_by_length_of_N(self, matched_substrings, locations, N):
        number_of_locations_found = len(locations)
        matched_substrings_filtered, locations_filtered = [], []

        for i in range(0, number_of_locations_found):
            index_start_end = locations[i]
            start, end = index_start_end[0], (index_start_end[1] - 1)
            if (((end + 1) - start) == N):
                matched_substrings_filtered.append(matched_substrings[i])
                locations_filtered.append(locations[i])

        return [matched_substrings_filtered, locations_filtered]


    def find_N_alphabets_in_target_string(self, target_string, N, mode = 'IGNORECASE'):
        [matched_substrings, locations] = self.find_alphabets_in_target_string(target_string, mode)
        [matched_substrings_with_N_alphabets, locations_with_N_alphabets] = self.filter_by_length_of_N(matched_substrings, locations, N)

        return [matched_substrings_with_N_alphabets, locations_with_N_alphabets]

    def find_N_numbers_in_target_string(self, target_string, N):
        [matched_substrings, locations] = self.find_numbers_in_target_string(target_string)
        [matched_substrings_with_N_numbers, locations_with_N_numbers] = self.filter_by_length_of_N(matched_substrings, locations, N)

        return [matched_substrings_with_N_numbers, locations_with_N_numbers]

    def find_N_ascii_symbols_in_target_string(self, target_string, N):
        [matched_substrings, locations] = self.find_ascii_symbols_in_target_string(target_string)
        [matched_substrings_with_N_ascii_symbols, locations_with_N_ascii_symbols] = self.filter_by_length_of_N(matched_substrings, locations, N)

        return [matched_substrings_with_N_ascii_symbols, locations_with_N_ascii_symbols]

    def find_alphabets_in_target_string(self, target_string, mode = 'IGNORECASE'):
        if (mode == 'IGNORECASE'):
            regex = re.compile(r'([a-z]+)', re.IGNORECASE) # ignore case
        elif (mode == 'UPPERCASE'):
            regex = re.compile(r'([A-Z]+)')  #
        elif (mode == 'LOWERCASE'):
            regex = re.compile(r'([a-z]+)')  #
        else:
            pass

        matched_substrings, locations = self.get_matched_substrings_found_and_locations(regex, target_string)

        return [matched_substrings, locations]

    def find_numbers_in_target_string(self, target_string):
        regex = re.compile(r'([0-9]+)')
        matched_substrings, locations = self.get_matched_substrings_found_and_locations(regex, target_string)

        return [matched_substrings, locations]

    def find_ascii_symbols_in_target_string(self, target_string):
        regex = re.compile(r'([^\w]+)')
        matched_substrings, locations = self.get_matched_substrings_found_and_locations(regex, target_string)

        return [matched_substrings, locations]

    def remove_alphabets_from_target_string(self, target_string, mode = 'IGNORECASE'):
        if (mode == 'IGNORECASE'):
            string_filtered = re.sub(r'[a-zA-Z]+', '', target_string)  # replace with nothing ''
        elif (mode == 'UPPERCASE'):
            string_filtered = re.sub(r'[A-Z]+', '', target_string)  # replace with nothing ''
        elif (mode == 'LOWERCASE'):
            string_filtered = re.sub(r'[a-z]+', '', target_string)  # replace with nothing ''
        else:
            pass

        return string_filtered

    def remove_numbers_from_target_string(self, target_string):
        string_filtered = re.sub("\d+", '', target_string) # replace with nothing ''

        return string_filtered

    def remove_ascii_symbols_from_target_string(self, target_string):
        string_filtered = re.sub(r'[^\w]', '', target_string) # replace with nothing ''

        return string_filtered

    def who_am_i(self):  #
        """ Introspection """
        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id)

####################################
## main
####################################
if __name__ == "__main__":
    id_regex_lib = "Library Agent: Internal Agent <regex_lib>"
    print("=====[" + id_regex_lib + " Start]===== \n")
    regex_lib_object = regex_lib(id_regex_lib)
    regex_lib_object.who_am_i()


    # import _Gaia._gaia
    # help(regex_lib) # introspect

    print("=====[" + id_regex_lib + " End]===== \n");

"""
# version: 2018-02-17_1344hr_09sec
"""