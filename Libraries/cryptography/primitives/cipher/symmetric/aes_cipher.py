from Crypto.Cipher import AES
from Crypto import Random

import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

# ref: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.modes.GCM

import codecs

number_of_bytes = 16
pad = lambda s: s + (number_of_bytes - len(s) % number_of_bytes) * chr(number_of_bytes - len(s) % number_of_bytes)
unpad = lambda s : s[0:-(s[-1])]

class aes_cipher:
    key = None

    def __init__( self, id = "aes_cipher"):
        self.id = id

    # ====== CBC ========
    def pad_bytes (self, byte_array_object):
        number_of_bytes = 16
        byte_array_object_padded = byte_array_object + b"0"*(number_of_bytes - len(byte_array_object) % number_of_bytes)
        print("length of byte_array_object_padded = ", len(byte_array_object_padded))
        return byte_array_object_padded

    def unpad_bytes (self, byte_array_object, iv):
        byte_array_object_unpadded = byte_array_object[0:-(len(iv)-2)]
        print("length of byte_array_object_padded = ", len(byte_array_object_unpadded))
        return byte_array_object_unpadded

    def generate_IV (self):
        iv = Random.new().read(AES.block_size)
        return iv

    def set_key_with_hex_string (self, key):
        self.key = codecs.decode(key, "hex")  # Requires hex encoded param as a key
        return None

    def generate_nonce (self, number_of_bytes):
        nonce = os.urandom(number_of_bytes)
        return nonce

    # ====== CBC ========
    def encrypt_cbc(self, key, plaintext):  # non-continous ciphering, i.e. only once, else use update()
        iv = self.generate_nonce(16)  # Generate a random 96-bit (12 bytes) IV.
        plaintext = self.pad_bytes(plaintext) # caveat: insecure padding

        # Construct an AES-CBC Cipher object with the given key and a randomly generated IV.
        encryptor = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        ).encryptor()

        # Encrypt the plaintext and get the associated ciphertext. GCM does not require padding.
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        return (iv, ciphertext)

    def decrypt_cbc(self, key, iv, ciphertext): # non-continous ciphering, i.e. only once, else use update()
        decryptor = Cipher( # Construct a Cipher object, with the key, iv.
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        ).decryptor()

        # Decryption gets us the authenticated plaintext.
        return decryptor.update(ciphertext) + decryptor.finalize()

    def encrypt_cbc_0(self, raw): # non-continous ciphering, i.e. only once, else use update()
        """
        Returns hex encoded encrypted value!
        """
        raw = pad(raw)
        # iv = self.generate_IV()
        iv = bytes([0]*number_of_bytes) # zeros for testing only
        print(iv)
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return codecs.encode(( iv + cipher.encrypt( raw ) ), "hex")

    def decrypt_cbc_0(self, enc): # non-continous ciphering, i.e. only once, else use update()
        """
        Requires hex encoded param to decrypt
        """
        enc = codecs.decode(enc, "hex")
        iv = enc[:number_of_bytes]
        enc= enc[number_of_bytes:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc))

    # ====== GCM ========
    def encrypt_gcm(self, key, plaintext, associated_data): # non-continous ciphering, i.e. only once, else use update()
        iv = self.generate_nonce(12) # Generate a random 96-bit (12 bytes) IV.

        encryptor = Cipher( # Construct an AES-GCM Cipher object with the given key and a randomly generated IV.
            algorithms.AES(key),
            modes.GCM(iv),
            backend=default_backend()
        ).encryptor()

        # associated_data will be authenticated but not encrypted, it must also be passed in on decryption.
        encryptor.authenticate_additional_data(associated_data)

        # Encrypt the plaintext and get the associated ciphertext. GCM does not require padding.
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        return (iv, ciphertext, encryptor.tag)

    def decrypt_gcm(self, key, associated_data, iv, ciphertext, tag): # non-continous ciphering, i.e. only once, else use update()
        # Construct a Cipher object, with the key, iv, and GCM tag used for authenticating the message.
        decryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
            backend=default_backend()
        ).decryptor()

        # We put associated_data back in or the tag will fail to verify when we finalize the decryptor.
        decryptor.authenticate_additional_data(associated_data)

        # Decryption gets us the authenticated plaintext.
        # If the tag does not match an InvalidTag exception will be raised.
        return decryptor.update(ciphertext) + decryptor.finalize()

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);

# main
if __name__== "__main__":
    key = "140b41b22a29beb4061bda66b6747e14"
    ciphertext = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81";
    key=key[:(2*number_of_bytes)]
    aes_cipher_object = aes_cipher(key)



