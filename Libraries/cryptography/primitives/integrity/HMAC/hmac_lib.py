from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac

class hmac_lib:
    key = None

    def __init__( self, id = "sha2"):
        self.id = id

    def hmac_sha256(self, key, byte_array_object): # non-continous
        h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        h.update(byte_array_object) # b"abc"
        hmac_result = h.finalize()
        return hmac_result

    def hmac_sha384(self, key, byte_array_object): # non-continous
        h = hmac.HMAC(key, hashes.SHA384(), backend=default_backend())
        h.update(byte_array_object)
        hmac_result = h.finalize()
        return hmac_result

    def hmac_sha512(self, key, byte_array_object): # non-continous
        h = hmac.HMAC(key, hashes.SHA512(), backend=default_backend())
        h.update(byte_array_object)
        hmac_result = h.finalize()
        return hmac_result

    def hmac_sha2_verify(self, hmac_context, hmac_result_to_be_verified):  # non-continous
        try:
            status = hmac_context.verify(hmac_result_to_be_verified) # b"an incorrect signature"
        except:
            status = 'Signature did not match digest.'

        if (status == None):
            status = 'Signature match digest.'

        return status

    def hmac_sha256_verify(self, hmac_result_to_be_verified, key, byte_array_object): # non-continous
        hmac_context = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        hmac_result = hmac_context.update(byte_array_object) # b"abc"
        # hmac_result = hmac_context.finalize()
        status = self.hmac_sha2_verify(hmac_context, hmac_result_to_be_verified)
        return status

    def hmac_sha384_verify(self, hmac_result_to_be_verified, key, byte_array_object): # non-continous
        hmac_context = hmac.HMAC(key, hashes.SHA384(), backend=default_backend())
        hmac_result = hmac_context.update(byte_array_object)
        status = self.hmac_sha2_verify(hmac_context, hmac_result_to_be_verified)
        return status
    
    def hmac_sha512_verify(self, hmac_result_to_be_verified, key, byte_array_object): # non-continous
        hmac_context = hmac.HMAC(key, hashes.SHA512(), backend=default_backend())
        hmac_result = hmac_context.update(byte_array_object)
        status = self.hmac_sha2_verify(hmac_context, hmac_result_to_be_verified)
        return status

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);

# main
if __name__== "__main__":
    data = b"140b41b22a29beb4061bda66b6747e14"
    data = b""
    id = "Library Agent: Internal Agent <sha2>"
    print("=====[" + id + " Start]===== \n")
    hmac_lib_object = hmac_lib(id)
