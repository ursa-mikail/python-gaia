import os
from pbkdf2 import crypt

import hashlib, binascii
import codecs

#
class KDF_lib:
    """ Template model of Gaia """
    id = "KDF_lib"

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id);

    def generate_hmac_with_pbkdf2 (self, passcode_hex_string, salt_hex_string, number_of_iterations, sha_algorithm = 'sha256'): # b'password', b'salt', 100000)
        passcode = passcode_hex_string.encode('ascii')
        salt = salt_hex_string.encode('ascii')
        hmac_result_bytes = hashlib.pbkdf2_hmac(sha_algorithm, passcode, salt, number_of_iterations)
        # print(type(hmac_result_bytes))
        hmac_result_hex_bytes = codecs.encode(hmac_result_bytes, 'hex')
        hmac_result_hex_string = hmac_result_hex_bytes.decode('ascii')

        return hmac_result_hex_string

    def is_valid_hmac(self, sha_algorithm, passcode_hex_string, salt_hex_string, number_of_iterations, hmac_in_DB):
        passcode = passcode_hex_string.encode('ascii')
        salt = salt_hex_string.encode('ascii')
        hmac_result_bytes = hashlib.pbkdf2_hmac(sha_algorithm, passcode, salt, number_of_iterations)
        hmac_result_hex_bytes = codecs.encode(hmac_result_bytes, 'hex')
        hmac_result_hex_string = hmac_result_hex_bytes.decode('ascii')

        return (hmac_result_hex_string == hmac_in_DB)

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
    id_KDF_lib = "Library Agent: Internal Agent <KDF_lib>"
    print("=====[" + id_KDF_lib + " Start]===== \n")
    KDF_lib_object = KDF_lib(id_KDF_lib)
    KDF_lib_object.who_am_i()

    # import _Gaia._gaia
    # help(KDF_lib) # introspect

    print("=====[" + id_KDF_lib + " End]===== \n");

"""
# version: 2018-01-14_1744hr_36sec
"""