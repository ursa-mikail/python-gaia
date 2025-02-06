####################################
import os, sys, re

# point to path
lib_path = os.path.abspath('../../Libraries/text')
sys.path.append(lib_path)

# import package from path
from text_processor import text_processor	# file name
'''
text processing i.e. remove empty lines, find/ substitute text, etc
'''

# data values are changed by this module
class field_variables_extractor:
    """ Template model of Gaia """
    id = "Utility Agent: Internal Agent <text_processor>"
    #print("=====[" + id + " Start]===== \n")

    inventory = {};
    inventory_id = "";

    def __init__(self, id):
        self.id = id
        self.text_processor_object = text_processor(id)
        print ("_gaia object [%s] is born\n" % self.id)

    def get_user_ids(self, contents):
        user_ids = []
        start, end = '(', ')'
        start, end = '\(', '\)'

        for i in range(0, len(contents)):
            line = contents[i]
            # result = line[line.find(start)+len(start):line.rfind(end)]
            # result = find_between_embedded_within_another( line, start, end )
            result = self.text_processor_object.find_multiple_occurrences_of_string_between_tags_with_embedded_contents(line, start, end)
            # print(result)
            # if (len(result) != 0):
            #    user_ids.append(result)
            for j in range(0, len(result)):
                user_ids.append(result[j])

        return user_ids

    def get_email_addresses(self, contents):
        email_addresses = []

        for i in range(0, len(contents)):
            line = contents[i]
            # match = re.search(r'[\w\.-]+@[\w\.-]+', line)
            # print(match)

            # if (match):
            #    email_addresses.append(match.group(0))

            matches = re.findall(r'[\w\.-]+@[\w\.-]+', line, re.DOTALL)
            # print(matches)
            for j in range(0, len(matches)):
                email_addresses.append(matches[j])

        return email_addresses

    def get_date_time(self, line):
        date_time = []
        demarcator = '-\/:._'
        number_of_characters_for_year, number_of_characters_for_month, number_of_characters_for_day = 4, 2, 2
        date_time_reg_exp = re.compile(r'\d{' + str(number_of_characters_for_year) + '}['+ demarcator +']\d{' + \
                                       str(number_of_characters_for_month) + \
                                       '}['+ demarcator +']\d{' + str(number_of_characters_for_day) + '}[^\s\n]*') # , re.DOTALL)

        # date_time_reg_exp = re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}')
        # date_time_reg_exp = re.compile('\d{4}[-/:._]\d{2}[-/:._]?\d{2}\S*')
        # date_time_reg_exp = re.compile(r'\d{4}[-/:._]\d{2}[-/:._]?\d{2}[^\s\n]*')
        matches_list = date_time_reg_exp.findall(line)

        for match in matches_list:
            date_time.append(match)

        return date_time

    def get_ip_addresses(self, line):
        ip_addresses = []
        matches_list = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)

        for match in matches_list:
            ip_addresses.append(match)

        return ip_addresses

    def get_file_url_path(self, line):
        file_url_path = []

        # regex = r'(?P<url>((https|ftp|file):\\/\\/)|(\\w*\\.\\w*\\.\\w*).*)|(?P<file>\\w:\\/\\/.*)'
        # regex = r"(?i)([a-z]:\/\/[^\/]+\/\S*)|((?:https?:\/\/)?(?:www\.)?[a-z0-9_-]+[.][a-z0-9_-]+\S*)|((?:ftp:\/\/)\S*)"
        # regex = r'^((https|ftp|file)?([Cc])?:\/\/)?(www.)?'
        regex = r'(?:http|http|www|ftp|[a-zA-Z]{1}:)\S+'
        # regex = r'(?:[a-zA-Z]{1}:)\S+'
        # regex = r'/(?i)\b([a-z]:\/\/[^\/]+\/\S*)|\b((?=.*https?:\/\/\w+\.\w+|.*www\.\w+\.\w+)(?:https?:\/\/)?(?:www\.)?[a-z]\w+\.\w+\S{3,})|(?:\/[a-z]\w+)*/gm'
        # regex = r"(?i)\b([a-z]:\/\/[^\/]+\/\S*)|\b((?=.*https?:\/\/\w+\.\w+|.*www\.\w+\.\w+)(?:https?:\/\/)?(?:www\.)?[a-z]\w+\.\w+\S{3,})|((?:\/[a-z]\w+){1,})"
        # regex = r"(?i)\b([a-z]:\/\/[^\/]+\/\S*)|\b((?=.*https?:\/\/\w+\.\w+|.*www\.\w+\.\w+)(?:https?:\/\/)?(?:www\.)?[a-z]\w+\.\w+\S{3,})|((?:\/[a-z]\w+){2,})"

        match_list = re.findall(regex, line, re.M)

        for match in match_list:
            file_url_path.append(match)


        return file_url_path

    def get_hex_values(self, line):
        hex_values = []
        matches_list = re.findall(r'0?[xX]?[0-9a-fA-F]+', line)

        for match in matches_list:
            hex_values.append(match)

        return hex_values

    def get_binary_values(self, line):
        binary_values = []
        # matches_list = re.findall(r'^[01]+$', line, re.DOTALL)
        matches_list = re.findall(r'0?b?[01]+', line, re.DOTALL) # with 0b prefix

        for match in matches_list:
            binary_values.append(match)

        return binary_values

    def who_am_i(self): #
        """ Introspection """
        self.line_storage = [];

        print ("My name is Gaia [" + self.id + "].")
        print("Field format interpretator")

        return

    def __del__(self):
        print ("_gaia object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id = "Utility Agent: Internal Agent <field_variables_extractor>"
    print ("=====[" + id + " Start]===== \n")
    field_variables_extractor_object = field_variables_extractor(id)
    field_variables_extractor_object.who_am_i()

    start, end = '\(', '\)'
    # start, end = '\[', '\]'
    # start, end = 'see', 'me'
    line = "-(123) = (45(test)6) = (789)- [123] + [455] **** [ok] see iii me see mmm me"
    items_found = field_variables_extractor_object.text_processor_object.find_multiple_occurrences_of_string_between_tags_with_embedded_contents(line, start, end)
    print(items_found)

    #import _Gaia._gaia
    #help(text_processor) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2019-07-27_2151hr_33sec
"""