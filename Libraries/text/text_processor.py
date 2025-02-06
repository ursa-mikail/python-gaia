'''
text processing i.e. remove empty lines, find/ substitute text, etc
'''
import re

# data values are changed by this module
class text_processor:
    """ Template model of Gaia """
    id = "text_processor"
    inventory = {};
    inventory_id = "";

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id);

    def remove_white_spaces(self, statement): #
        """ remove white spaces """
        statement = statement.replace("	", ""); # remove tabs
        statement_without_white_space = statement.replace(" ", ""); # remove space
        return statement_without_white_space;

    def remove_prepending_white_spaces(self, statement):
        """ remove white spaces before the string """
        statement_with_prepending_white_space_removed = statement.lstrip();
        return statement_with_prepending_white_space_removed;

    def remove_appending_white_spaces(self, statement):
        """ remove white spaces after the string """
        statement_with_appending_white_space_removed = statement.rstrip();
        return statement_with_appending_white_space_removed

    def remove_prepending_and_appending_white_spaces(self, statement):
        """ remove white spaces before and after the string """
        statement_with_prepending_appending_white_space_removed = statement.lstrip();
        statement_with_prepending_appending_white_space_removed = statement_with_prepending_appending_white_space_removed.rstrip();
        return statement_with_prepending_appending_white_space_removed;

    def is_empty_line(self, statement): #
        """ check for empty lines """
        if re.match(r'^\s*$', statement):	# line is empty (has only the following: \t\n\r and whitespace)
            return True;
        else:
            return False;

    def truncate_string_that_appears_before_tag(self, string_target, tag_string):
        """ remove string that appears before the given tag string """
        string_target_after_split = string_target.split(tag_string)
        number_of_elements = len(string_target_after_split)
        return string_target_after_split[number_of_elements-1] # return the last element

    def truncate_string_that_appears_after_tag(self, string_target, tag_string):
        """ remove string that appears before the given tag string """
        # truncate before the given tag
        string_target_after_split = string_target.split(tag_string)
        number_of_elements = len(string_target_after_split)
        return string_target_after_split[0] # return the 1st element

    def extract_string_between_tags(self, string_target, tag_string_front, tag_string_behind):
        """ extract string between given tag strings """
        string_target_after_front_removal = self.truncate_string_that_appears_before_tag(string_target, tag_string_front)
        string_target_after_back_removal = self.truncate_string_that_appears_after_tag(string_target_after_front_removal, tag_string_behind);
        return string_target_after_back_removal

    def ensure_no_prepending_tag (self, string_target, tag_delimiter):
        string_formatted = string_target # yet to be formatted

        if (len(string_formatted) != 0):
            while(string_formatted[0:(len(tag_delimiter))] == tag_delimiter):
                string_formatted = string_formatted.lstrip(tag_delimiter)
                if (len(string_formatted) == 0):
                    break

        return string_formatted

    def ensure_no_appending_tag (self, string_target, tag_delimiter):
        string_formatted = string_target # yet to be formatted

        if (len(string_formatted) != 0):
            while(string_formatted[len(string_formatted)-len(tag_delimiter):len(string_formatted)] == tag_delimiter):
                string_formatted = string_formatted.rstrip(tag_delimiter)
                if (len(string_formatted) == 0):
                    break

        return string_formatted

    def string_to_tokenized_list (self, string_target, tag_delimiter):
        tokenized_list = []

        return tokenized_list

    def replace_text (self, string_target, string_to_be_replaced, string_to_replaced_with):
        string_target_modified = string_target.replace(string_to_be_replaced, string_to_replaced_with)

        return string_target_modified

    def if_substring_exists (self, string_target, substring):
        status = False
        if substring in string_target:
            status = True

        return status

    def if_substrings_exist (self, string_target, substring_list):
        status = False

        for i in range(0, len(substring_list)):
            substring = substring_list[i]
            status = self.if_substring_exists(string_target, substring)
            if(status == False):	# even if 1 is missing, stop
                break
            else:
                pass

        return status

    """	
    def operation_on_1_array_or_matrix (self, array_or_matrix, operation_chosen):
        if (operation_chosen == self.operation_unary_options[0]):
            martix_resultant = np.reciprocal(array_or_matrix) # numpy.reciprocal() returns the reciprocal of argument, element-wise. For elements with absolute values > 1, the result is always 0 because of the way in which Python handles integer division. For integer 0, an overflow warning is issued.	
        if (operation_chosen == self.operation_unary_options[1]):
            martix_resultant = np.floor(array_or_matrix)
        if (operation_chosen == self.operation_unary_options[2]):
            martix_resultant = np.ceil(array_or_matrix)
        if (operation_chosen == self.operation_unary_options[3]):
            martix_resultant = np.round(array_or_matrix)
            
        return martix_resultant
    """

    # read file and filter text from excluded list
    def read_file_return_keyword(self, file_to_read_from, exclude_list):
        with open(file_to_read_from, "r") as txtfile:
            content = txtfile.readlines()
            # remove whitespace characters like `\n` at the end of each line
            # put all as lower case
            content = [x.lower().strip() for x in content]

        # untokenized
        # print (content)

        txtfile.close();

        # tokenized and filter from keyword excluded list
        """	
        exclude_list_set = set(['Mary', 'Jack', 'Jill', 'i', 'it'])
        """
        # '\''
        exclude_symbol_list = ['-', '_', '\t', ',', '\"', '!', '.', ';', '?', '-', '_', '(', ')']
        exclude_list_set = set(exclude_list);
        # exclude_list_set = exclude_list;
        # print (exclude_list_set)
        filtered_tokens = []

        for sentence in content:
            words = sentence.split()  # split words for every line
            # Optionally sort out some words
            for word in words:
                # filter symbols from the word
                for i in range(0, len(exclude_symbol_list)):
                    if exclude_symbol_list[i] in word:
                        word = word.replace(exclude_symbol_list[i], "")  # remove symbol

                if word in exclude_list_set:
                    # words.remove(word)
                    pass;
                # filtered_tokens.append('\'' + '\' \''.join(words) + '\'')
                else:
                    filtered_tokens.append(word)

        return filtered_tokens

    def find_string_between_tags(self, line, start_tag, last):
        try:
            start = line.index(start_tag) + len(start_tag)
            end = line.index(last, start)
            return line[start:end]
        except ValueError:
            return ""

    def find_string_between_tags_embedded_within_another(self, line, start_tag, end_tag):
        try:
            start = line.rindex(start_tag) + len(start_tag)
            end = line.rindex(end_tag, start)
            return line[start:end]
        except ValueError:
            return ""

    # always use this first, then use find_between_embedded_within_another()
    def find_multiple_occurrences_of_string_between_tags(self, line, start_tag, end_tag):
        # result = re.findall(r"(\([^']*\))", line)
        result = re.findall(r"" + start_tag + "[^']*?" + end_tag, line)

        # for i in result:
        #    print(i)

        return result

    def find_multiple_occurrences_of_string_between_tags_with_embedded_contents(self, line, start_tag, end_tag):
        result = self.find_multiple_occurrences_of_string_between_tags(line, start_tag, end_tag)

        if (start_tag == '\(' or '\['):
            start_tag = start_tag.lstrip('\\')

        if (end_tag == '\)' or '\]'):
            end_tag = end_tag.lstrip('\\')

        items_found = []

        for i in range(0, len(result)):
            ans = self.find_string_between_tags_embedded_within_another(result[i], start_tag, end_tag)
            items_found.append(ans)

        return items_found

    def who_am_i(self): #
        """ Introspection """
        self.line_storage = [];

        print ("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print ("_gaia object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <text_processor>"
    print ("=====[" + id + " Start]===== \n")
    text_processor_object = text_processor(id)
    text_processor_object.who_am_i()



    #import _Gaia._gaia
    #help(text_processor) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2019-07-27_2151hr_33sec
"""		