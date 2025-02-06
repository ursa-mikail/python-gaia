from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class sha2_lib:
    key = None

    def __init__( self, id = "sha2"):
        self.id = id

    def sha256(self, byte_array_object): # non-continous
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(byte_array_object) # b"abc"
        hash = digest.finalize()
        return hash

    def sha384(self, byte_array_object): # non-continous
        digest = hashes.Hash(hashes.SHA384(), backend=default_backend())
        digest.update(byte_array_object)
        hash = digest.finalize()
        return hash

    def sha512(self, byte_array_object): # non-continous
        digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
        digest.update(byte_array_object)
        hash = digest.finalize()
        return hash

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);

# main
if __name__== "__main__":
    data = b"140b41b22a29beb4061bda66b6747e14"
    data = b""
    id = "Library Agent: Internal Agent <sha2>"
    print("=====[" + id + " Start]===== \n")
    sha2_lib_object = sha2_lib(id)
    hash = sha2_lib_object.sha256(data)
    print(hash)
    print(hash[0])