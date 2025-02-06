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
    key = "140b41b22a29beb4061bda66b6747e14"
    ciphertext = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81";

    id_aes_cipher = "Usage Agent: <aes_cipher>"
    print("=====[" + id_aes_cipher + " Start]===== \n")
    aes_cipher_object = aes_cipher(id_aes_cipher)
    aes_cipher_object.set_key_with_hex_string(key)

    # import _Gaia._gaia
    # help(aes_cipher) # introspect

    plaintext = aes_cipher_object.decrypt_cbc_0(ciphertext)
    print("%s" % plaintext)
    plaintext_string = plaintext.decode("utf-8")
    plaintext_hex = "".join("{:02x}".format(ord(c)) for c in plaintext_string)
    print("plaintext_hex: ", plaintext_hex)
    # print("%s" % plaintext_hex)
    ciphertext = aes_cipher_object.encrypt_cbc_0(plaintext_hex)
    print("%s" % ciphertext)
    plaintext = aes_cipher_object.decrypt_cbc_0(ciphertext)

    # TEXT
    id_data_formatter = "Usage Agent: <data_formatter>"
    print("=====[" + id_data_formatter + " Start]===== \n")
    data_formatter_object = data_formatter(id_data_formatter)

    operation_unary_options = ['int_to_hex', 'hex_to_int', 'int_to_bin', 'bin_to_int', 'int_to_ascii', 'ascii_to_int',
                               'string_to_base64', 'base64_to_string']

    operation_chosen = operation_unary_options[5]

    ascii_string = "Hello, I am Ursa Major"
    int_array = data_formatter_object.data_conversion_on_array(ascii_string, operation_chosen)
    print(int_array)
    operation_chosen = operation_unary_options[0]
    hex_array = data_formatter_object.data_conversion_on_array(int_array, operation_chosen)
    print(hex_array)
    byte_values = bytes(int_array)
    byte_values_hex = binascii.hexlify(byte_values)
    print(byte_values_hex)
    byte_values_hex_string = byte_values_hex.decode("utf-8")
    print(byte_values_hex_string)
    hex_string_byte_array = bytearray.fromhex(byte_values_hex_string)
    print("hex_string_byte_array: ", hex_string_byte_array)
    hex_string = binascii.hexlify(hex_string_byte_array)
    print(hex_string)
    hex_string = hex_string.decode("utf-8")
    print(hex_string)

    # symmetric CBC
    import os
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend

    backend = default_backend()
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(b"a secret message") + encryptor.finalize()
    print("ct", ct)

    decryptor = cipher.decryptor()
    print(decryptor.update(ct) + decryptor.finalize())

    print("=====[" + id_aes_cipher + " End]===== \n");


"""
# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.modes.GCM

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305

data = b"a secret message"
aad = b"authenticated but unencrypted data"

nonce = os.urandom(12)

#key = ChaCha20Poly1305.generate_key()
#chacha = ChaCha20Poly1305(key)
#ct = chacha.encrypt(nonce, data, aad)
#chacha.decrypt(nonce, ct, aad)

bit_length = 256

key = AESGCM.generate_key(bit_length=bit_length)
aesgcm = AESGCM(key)
ct = aesgcm.encrypt(nonce, data, aad)
print(ct)
pt = aesgcm.decrypt(nonce, ct, aad)
print(pt)

# =====================================================================
# symmetric cipher
from cryptography.fernet import Fernet

def keygeneration():
    key = Fernet.generate_key()
    f = Fernet(key)
    print("the key is ", key)
    return f

def encryption(f, textToEncrypt):
    encryptedText = f.encrypt(textToEncrypt)
    print("the encrypted text is ", encryptedText)
    return encryptedText


def decryption(f, encryptedText):
    decryptedText = f.decrypt(encryptedText)
    print("the decrypted text is ", decryptedText)


print("Enter text to encrypt")
textToEncrypt = input()
bytes('example', encoding='utf-8')
textToEncrypt = bytes(textToEncrypt, encoding='utf-8')
f = keygeneration()
encryptedText = encryption(f, textToEncrypt)
decryption(f, encryptedText)

# HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
key = b'1234567812345678'
h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
h.update(b"message to hash")
print(h.finalize())

# hash
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

digest.update(b"abc")
hash1 = digest.finalize()
print("hash of \"abc\" is\n", hash1)

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"1234567890")
hash2 = digest.finalize()
print("hash of \"1234567890\" is\n", hash2)

# symmetric ECB
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)

# iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret messagea secret message")
print(ct)
decryptor = cipher.decryptor()
x = decryptor.update(ct)
y = ct[0:16]
z = ct[16:32]
print("\n\n\n\n")
print("1st block ", y, "\t", x[0:16])
print("2nd block ", z, "\t", x[16:32])

# 
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret messagea secret message")
print("IV1 used is ", iv) 
print(ct)
decryptor = cipher.decryptor()
x = decryptor.update(ct)
y = ct[0:16]
z = ct[16:32]
print("\n\n\n\n")
print("1st block ", y, "\t", x[0:16])
print("2nd block ", z, "\t", x[16:32])

print("\n\n\n")
iv2 = os.urandom(16)
print("IV2 used is ", iv2)
cipher2 = Cipher(algorithms.AES(key), modes.CBC(iv2), backend=backend)
encryptor = cipher2.encryptor()
ct2 = encryptor.update(b"a secret messagea secret message")
print(ct2)
decryptor = cipher2.decryptor()
x = decryptor.update(ct2)
y = ct2[0:16]
z = ct2[16:32]
print("\n\n\n\n")
print("1st block ", y, "\t", x[0:16])
print("2nd block ", z, "\t", x[16:32])

# asymmetric cipher (verification)
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from pprint import pprint

private_key = dsa.generate_private_key(key_size=1024,
                                       backend=default_backend())

private_key1 = dsa.generate_private_key(key_size=1024,
                                        backend=default_backend())


print("private key is", private_key)
print("one more key", repr(private_key))
print("zzz", private_key.__str__())
signer = private_key.signer(hashes.SHA256())
data = b"this is some data I'd like to sign"
signer.update(data)
signature = signer.finalize()

public_key = private_key.public_key()
print("public key is", public_key)
verifier = public_key.verifier(signature, hashes.SHA256())
verifier.update(data)
verifier.verify()

"""

# https://github.com/pyca/cryptography/blob/master/docs/hazmat/primitives/aead.rst