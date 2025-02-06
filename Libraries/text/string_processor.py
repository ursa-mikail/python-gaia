'''

'''
####################################

class string_processor_class:
    """ Template model from Gaia """
    id = "";

    def __init__(self, id):
        self.id = id;
        print ("string_processor object [%s] is born\n" % self.id);

    def who_am_i(self): # read from file
        """ Introspection """
        self.line_storage = [];

        print ("My name is string_processor [", self.id,"].")

        return

    def string_to_tokens_given_delimiter(self, string_target, delimiter):
        list_tokenized = string_target.split(delimiter)

        return list_tokenized

    """
    Ensure No Appending Symbol on String 
    """
    def lstrip_ensure_no_symbol (self, symbols, str_target):
        while (str_target[0] in symbols):
            str_target = str_target[1:len(str_target)]; # cut off the 1st character

        return str_target;

    """
    Ensure No Trailing Symbol on String 
    """
    def rstrip_ensure_no_symbol (self, symbols, str_target):

        if (len(str_target) == 1):
            if (str_target[len(str_target) - 1] in symbols):
                str_target = str_target[0:len(str_target) - 1];  # cut off the 1st character

            return str_target

        if (len(str_target) == 0):
            return str_target

        while (str_target[len(str_target)-1] in symbols):
            if (len(str_target) != 0):
                str_target = str_target[0:len(str_target)-1]; # cut off the 1st character
            else:
                return str_target

            if (len(str_target) == 0):
                return str_target

        return str_target;

    def __del__(self):
        print ("string_processor object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    print ("=====[Internal Test Start]===== \n");
    id = "Internal Agent"
    string_processor_object = string_processor_class(id);
    string_processor_object.who_am_i();

    print ("=====[Internal Test End]===== \n");
