import os, sys
import binascii as binascii

# point to path
lib_path = os.path.abspath('../../../../../Libraries/cryptography/primitives/cipher/symmetric')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../../Libraries/data')
sys.path.append(lib_path)

# import package from path
from aes_cipher import aes_cipher	# file name
from data_formatter import data_formatter	#

####################################
## main
####################################
if __name__ == "__main__":
    id_aes_cipher = "Usage Agent: <aes_cipher>"
    print("=====[" + id_aes_cipher + " Start]===== \n")
    aes_cipher_object = aes_cipher(id_aes_cipher)
    # CBC
    plaintext, key = aes_cipher_object.generate_nonce(50), aes_cipher_object.generate_nonce(16)
    print("plaintext (before padding): %s" % plaintext)
    iv, ciphertext = aes_cipher_object.encrypt_cbc(key, plaintext)
    print("ciphertext: %s" % ciphertext)
    plaintext = aes_cipher_object.decrypt_cbc(key, iv, ciphertext)
    print("plaintext (before remove padding): %s" % plaintext)
    print("plaintext (remove padding): %s" % aes_cipher_object.unpad_bytes(plaintext, iv))

    # GCM
    number_of_bytes = 16
    plaintext, key, associated_data = b"a secret message!", aes_cipher_object.generate_nonce(number_of_bytes), b"authenticated but not encrypted payload"
    iv, ciphertext, tag = aes_cipher_object.encrypt_gcm(
        key,
        plaintext,
        associated_data
    )

    print(aes_cipher_object.decrypt_gcm(
        key,
        associated_data,
        iv,
        ciphertext,
        tag
    ))
    print("==================================================")
