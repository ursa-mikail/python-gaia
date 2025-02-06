import os
# import pycrypto

# from Crypto import pbkdf2

import hashlib, binascii
from pbkdf2 import crypt


def isValidPassword(userPassword, hashKeyInDB):
    result = crypt(userPassword, hashKeyInDB, iterations=1000)
    print (result)
    return (result == hashKeyInDB)  # hashKeyInDB in this case is $p5k2$3e8$her4h.6b$.p.OE5Gy4Nfgue4D5OKiEVWdvbxBovxm

"""
Provisioning profile: use a GUID (group ID) with secret and generate IIDs  (individual ) and FIDs (functional / services)

GUI = # group ID
IIDs = # individual IDs
FIDs = # function IDs
"""
ID = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
ID_hex = binascii.hexlify(ID)
print("ID_hex", ID_hex)

password_hash = crypt("secret", iterations=1000)
print (password_hash)


if isValidPassword("secret", password_hash):
    print("OK")
else:
    print("NOT OK")


"""
m = hashlib.sha256() # hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
m.block_size

Ref: http://bityard.blogspot.com/2012/08/symmetric-crypto-with-pycrypto-part-3.html

"""

