'''

'''
####################################
import subprocess
import os
import re

class keywords_grep_class:
    """ Template model from Gaia """
    id = "";

    def __init__(self, id):
        self.id = id;
        print ("keywords_grep object [%s] is born\n" % self.id);

    def who_am_i(self): # read from file
        """ Introspection """
        self.line_storage = [];

        print ("My name is keywords_grep [", self.id,"].")

        return

    def keywords_frequency(self, statement):
        word_list = [s.lower() for s in statement.split()]  # assume lower case words only
        word_count = [word_list.count(w) for w in word_list]
        dictionary_word_list_with_frequency = dict(zip(word_list, word_count))

        for item in dictionary_word_list_with_frequency:
            print("Word '%s' occurs %d times." % (item, dictionary_word_list_with_frequency[item]))

        return

    def filter_in_data_list_by_keywords (self, data_list, key_word_list):
        DOES_NOT_EXIST, EXIST = -1, 1
        STATUS = DOES_NOT_EXIST
        data_list_filtered = []

        for i in range(0, len(data_list)):
            for j in range(0, len(key_word_list)):
                if str(data_list[i]).find(key_word_list[j]) == DOES_NOT_EXIST:
                    pass;
                else:
                    STATUS = EXIST
                    break

            if (STATUS == EXIST):
                data_list_filtered.append(data_list[i])
                STATUS = DOES_NOT_EXIST # reset flag for the next scan

        return data_list_filtered

    def filter_out_data_list_by_keywords (self, data_list, key_word_list):
        DOES_NOT_EXIST, EXIST = -1, 1
        STATUS = DOES_NOT_EXIST
        data_list_filtered = []

        for i in range(0, len(data_list)):
            for j in range(0, len(key_word_list)):
                if str(data_list[i]).find(key_word_list[j]) == DOES_NOT_EXIST:
                    pass;
                else:
                    STATUS = EXIST
                    break

            if (STATUS == DOES_NOT_EXIST):
                data_list_filtered.append(data_list[i])

            STATUS = DOES_NOT_EXIST # reset flag for the next scan

        return data_list_filtered

    # read contents and grep (non-case sensitive)
    def read_contents_and_grep(self, keyword_input, page_contents_file): # only 1 keyword for trial test
        """ Introspection """
        statement = "grep -i \"" + keyword_input + "\" < " + page_contents_file;
        print (statement)

        hosts = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
        output = hosts.communicate();
        output_len = len(output);
        output_to_display = str(output[0]).lstrip("b'").rstrip("'");

        #print (output_to_display);
        output_array = output_to_display.split("\\r\\n");
        #output_array.remove(''); # remove empty element
        #print (output_array);
        #print (" : There are " + str(len(output_array)));

        return output_to_display;

    # grep string (non-case sensitive)
    def grep_string(self, keyword_input, string_target): # only 1 keyword for trial test
        """ Introspection """
        statement = "grep -i \"" + keyword_input + "\" <<< " + string_target;
        #print (statement)

        hosts = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
        output = hosts.communicate();
        output_len = len(output);
        output_to_display = str(output[0]).lstrip("b'").rstrip("'");

        #print (output_to_display);
        output_array = output_to_display.split("\\r\\n");
        #output_array.remove(''); # remove empty element
        #print (output_array);
        #print (" : There are " + str(len(output_array)));

        return output_to_display;

    # read keyword list
    def load_keywordlist (self, file_to_read_from):
        """ load keywordlist """
        line_counter = 0; # non-empty line counter
        keyword_list = [];

        with open(file_to_read_from, "r") as file_keywords:
            for line in file_keywords:
                # remove whitespaces
                #line_without_empty_spaces = os.linesep.join([s for s in line.splitlines() if s])
                line_without_empty_spaces = line.strip(' \t\n\r')

                if (len(line_without_empty_spaces) != 0): # non-empty line
                    line_counter = line_counter + 1;
                    line = line.strip('\n\r');
                    keyword_list.append(line);

        file_keywords.close();

        return [keyword_list, line_counter];

    def split_with_prefixes(self, word, prefixes):
        regex = re.compile('|'.join(sorted(prefixes, key=len, reverse=True)))
        result = []
        i = 0
        while True:
            mo = regex.match(word, i)
            if mo is None:
                result.append(word[i:])
                return result
            result.append(mo.group())
            i = mo.end()

        return;

    def split_with_symbols(self, string, symbols):
        str_tokens = list(string);
        string_unmet_with_symbol = ""; # continous string not meeting given symbol
        str_tokens_filtered = [];

        counter = 0;

        for character in str_tokens:
            counter = counter + 1;

            if (character not in symbols): #
                string_unmet_with_symbol = string_unmet_with_symbol + character;
            else:
                if (string_unmet_with_symbol != ""):
                    str_tokens_filtered.append(string_unmet_with_symbol);
                    string_unmet_with_symbol = "";

            if (counter == len(string)) & (character not in symbols): # end of string and without meeting given symbol
                if (string_unmet_with_symbol != ""):
                    str_tokens_filtered.append(string_unmet_with_symbol);
                    string_unmet_with_symbol = "";

        return str_tokens_filtered;

    # compute_sha256_on_string_contents_of_file : compute sha256 for string (in/excluding whitespaces)
    def compute_sha256_on_string_contents_of_file(self, file_to_read_from, mode = None):
        with open(file_to_read_from) as f:
            content = f.readlines()
            if (mode != None):
                if (mode.lower() == "without_whitespaces"):
                    # remove whitespace characters like `\n` at end of each line
                    content = [x.strip(' 	\t\n\r') for x in content]

        content = "".join(content); # list to string
        if (mode != None):
            if (mode.lower() == "without_whitespaces"):
                content = content.replace('\n','')
                content = content.replace('\r','')
                content = content.replace(' ','')
                content = content.replace('\t','')

        content = content.rstrip('\n')
        statement = "printf \"" + content + "\"| openssl dgst -sha256 "; # will not work if the string contents special characters
        # print (statement)

        hosts = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
        output = hosts.communicate();
        #output_len = len(output);
        output_to_display = str(output[0]).lstrip("b'").rstrip("'");
        output_to_display = output_to_display.replace('(stdin)=','')
        output_to_display = output_to_display.replace(' ','')
        output_to_display = output_to_display.replace('\\n','')

        #print (output_to_display);
        output_array = output_to_display.split("\\r\\n");
        #output_array.remove(''); # remove empty element
        #print (output_array);

        return output_to_display

    def compute_sha256_of_file(self, file_to_read_from):
        statement = "openssl dgst -sha256 " + file_to_read_from; # will not work if the string contents special characters
        # print (statement)

        hosts = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
        output = hosts.communicate();
        #output_len = len(output);
        output_to_display = str(output[0]).lstrip("b'").rstrip("'");
        output_to_display = output_to_display.replace('(stdin)=','')
        output_to_display = output_to_display.replace(' ','')
        output_to_display = output_to_display.replace('\\n','')

        output_to_display = output_to_display.split("=")[1]; # take the 2nd portion

        #print (output_to_display);
        output_array = output_to_display.split("\\r\\n");
        #output_array.remove(''); # remove empty element
        #print (output_array);

        return output_to_display

    # compute_sha256_on_string : compute sha256 for string (excluding whitespaces)
    def compute_sha256_on_string(self, string_target, mode = None):

        content = string_target;
        if (mode != None):
            if (mode.lower() == "without_whitespaces"):
                content = content.replace('\n','')
                content = content.replace('\r','')
                content = content.replace(' ','')
                content = content.replace('\t','')

        content = content.rstrip('\n')
        statement = "printf \"" + content + "\"| openssl dgst -sha256 ";
        print (statement)

        hosts = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
        output = hosts.communicate();
        #output_len = len(output);
        output_to_display = str(output[0]).lstrip("b'").rstrip("'");
        output_to_display = output_to_display.replace('(stdin)=','')
        output_to_display = output_to_display.replace(' ','')
        output_to_display = output_to_display.replace('\\n','')

        #print (output_to_display);
        output_array = output_to_display.split("\\r\\n");
        #output_array.remove(''); # remove empty element
        #print (output_array);

        return output_to_display

    def substring_without_prepending_whitespace_or_character_exist(self, pattern, line_target):
        pattern = r'^' + pattern + '.*'  # omitting anything before it
        STATUS_FOUND = re.findall(pattern, line_target)
        """
        pattern = r'^' + pattern + '.*' # omitting anything before it
        STATUS_FOUND =  = re.search(pattern, line_target)
        """
        return STATUS_FOUND

    def substring_with_prepending_whitespace_exist(self, pattern, line_target):
        pattern = r'^\s[' + pattern + '.*]'  # omitting anything before it
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    def substring_with_prepending_whitespace_or_character_exist(self, pattern, line_target):
        pattern = r'^(.+' + pattern + ')'
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    def substring_without_appending_whitespace_or_character_exist(self, pattern, line_target):
        pattern = r'(' + pattern + '$)'
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    def substring_with_appending_whitespace_or_character_exist(self, pattern, line_target):
        pattern = r'^(' + pattern + '.+)'
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    """
    e.g.
    #pattern = r'^cod.*' # omitting anything before it
    #pattern2 = r'^\s[cod.*]' # omitting anything before it
    \s matches a whitespace character.
    \S matches a non-whitespace character.
    """

    def substring_partial_exist(self, pattern_part_1, pattern_part_2, line_target):
        #rex = re.compile('th.s')
        #l = "this, thus, just, then"
        #print(rex.findall(l))

        pattern = r'' + pattern_part_1 + '.+' + pattern_part_2
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    def substring_partial_given_number_of_characters_inbetween_exist(self, pattern_part_1, pattern_part_2, number_of_characters_inbetween, line_target):
        # ^[A-Z]{1,10}$
        # pattern = r'' + pattern_part_1 + '\D{' + str(number_of_characters_inbetween) + '}' + pattern_part_2
        pattern = r'' + pattern_part_1 + '.{' + str(number_of_characters_inbetween) + '}' + pattern_part_2
        #print("pattern: ", pattern)
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    def substring_partial_given_range_of_number_of_characters_inbetween_exist(self, pattern_part_1, pattern_part_2, number_of_characters_inbetween_lower, number_of_characters_inbetween_upper, line_target):
        # ^[A-Z]{1,10}$
        # pattern = r'' + pattern_part_1 + '\D{' + str(number_of_characters_inbetween) + '}' + pattern_part_2
        pattern = r'' + pattern_part_1 + '.{' + str(number_of_characters_inbetween_lower) + ',' + str(number_of_characters_inbetween_upper) + '}' + pattern_part_2
        #print("pattern: ", pattern)
        STATUS_FOUND = re.findall(pattern, line_target)

        return STATUS_FOUND

    def find_all_substring_positions_in_line(self, pattern_target, string_target):
        positions_start = [m.start() for m in re.finditer(pattern_target, string_target)]
        positions_end = [len(pattern_target)]*len(positions_start)
        positions_end = [a + b for a, b in zip(positions_start, positions_end)] # element wise addition

        return positions_start, positions_end

    def tokenize_line_given_substring(self, pattern_target, string_target, option):
        positions_start, positions_end = self.find_all_substring_positions_in_line(pattern_target, string_target)

        NULLS_INCLUDED, NULLS_INCLUDED_NOT = True, False

        tokenize_line = []
        start = 0
        for i in range(0, len(positions_start)):
            end = positions_start[i]

            if option == NULLS_INCLUDED:
                tokenize_line.append(string_target[start:end])
                start = positions_end[i]
            else:
                #if(start != end):
                if (len(string_target[start:end]) != 0):
                    tokenize_line.append(string_target[start:end])

                start = positions_end[i]

        if (start < len(string_target)):
            tokenize_line.append(string_target[start:(len(string_target))])

        return tokenize_line

    def __del__(self):
        print ("keywords_grep object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    print ("=====[Internal Test Start]===== \n");
    id = "Internal Agent"
    keywords_grep_object = keywords_grep_class(id)
    keywords_grep_object.who_am_i()

    text = ['coding logic', ' codxing', 'codes', 'cod', 'codex', 'fucod', 'cxd']
    pattern = 'cod'

    for i in range(0, len(text)):
        # result = substring_without_prepending_whitespace_or_character_exist (pattern, text[i]) # or re.findall(pattern2, text[i])
        # result = substring_with_prepending_whitespace_exist (pattern, text[i])
        # result = substring_with_prepending_whitespace_or_character_exist (pattern, text[i])
        # result = substring_with_appending_whitespace_or_character_exist (pattern, text[i])
        result = keywords_grep_object.substring_without_appending_whitespace_or_character_exist(pattern, text[i])

        if result:
            print(text[i])
        else:
            print('NIL')

    print('======================================================')
    text = ['this', 'thus', 'just', 'then']
    text = ['thx01202801x:s', 'thuuOKuus', 'thQuuOKuu#%O>s', 'th01234567891s', 'just', 'th12345s', 'th123456s', 'th1234567s', 'th12345678s', 'then']
    number_of_characters = 6 # 11
    number_of_characters_inbetween_lower, number_of_characters_inbetween_upper = 5, 7
    pattern_part_1, pattern_part_2 = 'th', 's'
    for i in range(0, len(text)):
        # result = keywords_grep_object.substring_partial_exist(pattern_part_1, pattern_part_2, text[i])
        # result = keywords_grep_object.substring_partial_given_number_of_characters_inbetween_exist(pattern_part_1, pattern_part_2, number_of_characters, text[i])
        result = keywords_grep_object.substring_partial_given_range_of_number_of_characters_inbetween_exist(pattern_part_1, pattern_part_2, number_of_characters_inbetween_lower, number_of_characters_inbetween_upper, text[i])

        if result:
            print(text[i])
        else:
            print('NIL')

    NULLS_INCLUDED, NULLS_INCLUDED_NOT = True, False
    string_target = '",101,"test",101,"",101,"",101,"",101,"test",101,"test",101,"test",101,"'
    pattern_target = '",101,"'
    #string_target = '"test","","","","test","test","test",101,"'
    #pattern_target = '","'
    positions_start, positions_end = keywords_grep_object.find_all_substring_positions_in_line(pattern_target, string_target)

    for i in range(0, len(positions_start)):
        print(string_target[positions_start[i]:positions_end[i]])

    tokenize_line = keywords_grep_object.tokenize_line_given_substring(pattern_target, string_target, NULLS_INCLUDED)
    print (tokenize_line)

    print ("=====[Internal Test End]===== \n");
