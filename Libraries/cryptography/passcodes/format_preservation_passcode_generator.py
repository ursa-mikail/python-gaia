import pyffx

class format_preservation_passcode_generator:
    """ Template model of Gaia """
    id = "format_preservation_passcode_generator"

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id);

    def verify_recoverable_passcode(self, passcode_original, passcode_derived, ciphered_resultant, deciphered_resultant):
        print('[ciphered_resultant, deciphered_resultant] = ', ciphered_resultant, '\t', deciphered_resultant)

        if (passcode_original == passcode_derived):
            print('passcode_original, [ ', passcode_original, ' ], is recoverable')
        else:
            print('passcode_original, [ ', passcode_original, ' ], is NOT recoverable')

        assert (passcode_original == passcode_derived), (
        'passcode_original, [ ', passcode_original, ' ], is NOT recoverable')

        return None

    def FPE_cipher(self, secret_key, data, symbol_space=None):
        if (type(data) == int):
            len_data = len(str(data))
        else:
            len_data = len(data)

        if (symbol_space != None):
            cipher_handler = pyffx.String(secret_key, alphabet=symbol_space, length=len_data)
        else:
            cipher_handler = pyffx.Integer(secret_key, length=len_data)

        ciphered_resultant = cipher_handler.encrypt(data)

        return ciphered_resultant

    def FPE_decipher(self, secret_key, data, symbol_space=None):
        if (type(data) == int):
            len_data = len(str(data))
        else:
            len_data = len(data)

        if (symbol_space != None):
            cipher_handler = pyffx.String(secret_key, alphabet=symbol_space, length=len_data)
        else:
            cipher_handler = pyffx.Integer(secret_key, length=len_data)

        deciphered_resultant = cipher_handler.decrypt(data)

        return deciphered_resultant

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
    id = "Usage Agent: <format_preservation_passcode_generator>"
    print ("=====[" + id + " Start]===== \n")
    FPE_generator_object = format_preservation_passcode_generator(id)
    FPE_generator_object.who_am_i()