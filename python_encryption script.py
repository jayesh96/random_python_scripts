application_key = '6zCFNzuqbW'

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
public_key = key.publickey()
enc_data = public_key.encrypt(application_key, 32)






import os
import binascii
print(binascii.hexlify(os.urandom(32)))



from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
print key

key.can_encrypt()
key.can_sign()
key.has_private()

public_key = key.publickey()
enc_data = public_key.encrypt('abcdefgh', 32)
print enc_data
