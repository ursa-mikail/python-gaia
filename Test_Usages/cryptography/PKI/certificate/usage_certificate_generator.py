from pyasn1_modules import pem, rfc2459
from pyasn1.codec.der import decoder

from cryptography.hazmat.primitives.asymmetric import rsa


import os, sys

# point to path
lib_path = os.path.abspath('../../../../Libraries/data/trend')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../../Libraries/display/console')
sys.path.append(lib_path)

lib_path = os.path.abspath('../../../../Libraries/cryptography/PKI/certificate')
sys.path.append(lib_path)

# import package from path
from trend_profiler import trend_profiler	# file name
from data_generator import data_generator
from display_console import display_console	
from data_processor import data_processor
from certificate_generator import certificate_generator

from OpenSSL import crypto

TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA

number_of_bytes = 32

def initialize_object (object_type, object_ID):
	id_object = "Test Usage Agent: <" + object_ID + ">"
	print ("=====[" + id_object + " Start]===== \n")
	object = object_type(id_object)
	
	return object
	
def declare_object_end (object_ID):
	print ("=====[" + object_ID + " End]=====")
	
def init_cipher(key): # secret phrase with 32 bytes and iv to 16 bytes
	number_of_bytes = 32
	key = hashlib.sha256(key.encode()).digest()	
	
	return key
	
def _pad(s):
	return s + (number_of_bytes - len(s) % number_of_bytes) * chr(number_of_bytes - len(s) % number_of_bytes)

	@staticmethod
	def _unpad(s):
		return s[:-ord(s[len(s)-1:])]	
	
# reference: https://github.com/pyca/pyopenssl/tree/master/tests	
####################################
## main
####################################
if __name__ == "__main__":
	display_console_object = initialize_object (display_console, 'display_console')
	certificate_generator_object = initialize_object (certificate_generator, 'certificate_generator')
	
	path_to_certificates = './data/certificates/users/ursa/'
	certificate_file_names = ['ursa.cert.der']
	choice = 0
	certificate_file_chosen = certificate_file_names[choice]
	certificate_file_chosen = path_to_certificates + certificate_file_chosen
	
	certificate_generator_object.get_certificate_profile (certificate_file_chosen, crypto.FILETYPE_ASN1)
	
	[asymetric_key_type, key_integrity_algo, key_length] = [crypto.TYPE_RSA, 'sha256', 2048]
	
	certificate_object = certificate_generator_object.generate_asymetric_key_and_generate_certificate (asymetric_key_type, key_integrity_algo, key_length)
	
	public_key =  certificate_generator_object.get_public_key_from_certificate_object(certificate_object, crypto.FILETYPE_PEM)
	
	display_console_object.display_variable ('public_key', public_key)
	
	path_to_certificates = './data/certificates/trial/'
	
	certificate_file_to_write_to = "ursa_app.crt"
	private_key_file_to_write_to = "ursa_app_private_key.key"
	public_key_file_to_write_to = "ursa_app_public_key.key"
	
	[country, state, city, organization, org_unit, service_id, serial_number] = ['US', 'CA', 'Cupertino', 'Walnuss', 'Omen', 'Test site', 19751102]
	
	# validity period
	[year_allowable, day_per_year, hours_per_day, minutes_per_hour, seconds_per_minute] = [5, 365, 24, 60, 60]
	time_start_from_now_in_secs = 0
	time_end_from_now_in_secs = year_allowable*day_per_year*hours_per_day*minutes_per_hour*seconds_per_minute
	
	certificate_generator_object.create_self_signed_certificate(path_to_certificates, asymetric_key_type, key_integrity_algo, certificate_file_to_write_to, private_key_file_to_write_to, public_key_file_to_write_to, key_length, country, state, city, organization, org_unit, service_id, serial_number, (time_start_from_now_in_secs, time_end_from_now_in_secs))
	
	'''
	openssl x509 -in ./data/certificates/trial/ursa_app.crt -text -noout
	openssl rsa -in ./data/certificates/trial/ursa_app_private_key.key -check
	openssl rsa -in ./data/certificates/trial/ursa_app_public_key.key -check
	
	'''
	
	from asn1crypto.x509 import Certificate
	from os.path import exists, join
	
	with open(certificate_file_chosen, "rb") as f:
		cert = Certificate.load(f.read())
	
	n = cert.public_key.native["public_key"]["modulus"]
	e = cert.public_key.native["public_key"]["public_exponent"]
	
	print("{:#x}".format(n))    # prints the modulus (hexadecimal)
	print("{:#x}".format(e))    # the public exponent
	
	cakey = certificate_generator_object.create_key_pair(TYPE_RSA, key_length)
	# careq = certificate_generator_object.create_certificate_request(cakey, CN='Certificate Authority')
	"""
	C = 'US' #    - Country name
	ST = '' #    - State or province name
	L     - Locality name
	O     - Organization name
	OU    - Organizational unit name
	CN    - Common name
	emailAddress - E-mail address
	"""
	[C, ST, L, O, OU, CN, emailAddress] = ['US', 'CA', 'Cupertino', 'Walnuss', 'Omen', 'Walnuss.Omen', 'omen@walnuss.com']
	
	careq = certificate_generator_object.create_certificate_request(cakey, key_integrity_algo, C='US', ST='CA', L = 'Cupertino', O = 'Walnuss', OU = 'Omen', CN = 'Walnuss.Omen', emailAddress = 'omen@walnuss.com')
	
	cacert = certificate_generator_object.create_certificate(careq, (careq, cakey), serial_number, (time_start_from_now_in_secs, time_end_from_now_in_secs), key_integrity_algo) # N years
	
	path_to_certificates = './data/certificates/trial/'
	private_key_file_to_write_to = join(path_to_certificates, 'CA.private.key')
	certificate_file_to_write_to = join(path_to_certificates, 'CA.crt')
	
	certificate_generator_object.write_private_to_key_file ( cakey, private_key_file_to_write_to)
	
	private_key_file_to_read_from = private_key_file_to_write_to
	private_key_in_text = certificate_generator_object.read_key_from_key_file (private_key_file_to_read_from)
	
	display_console_object.display_variable("private_key_in_text", private_key_in_text)
	
	public_key_file_to_read_from = join(path_to_certificates, public_key_file_to_write_to)
	public_key_in_text = certificate_generator_object.read_key_from_key_file (public_key_file_to_read_from)
	
	display_console_object.display_variable("public_key_in_text", public_key_in_text)
	
	certificate_generator_object.write_certificate_to_certificate_file ( cacert, certificate_file_to_write_to)
	
	certificate_file_to_read_from = certificate_file_to_write_to

	certificate_generator_object.get_certificate_profile (certificate_file_to_read_from, crypto.FILETYPE_PEM)
	
	#
	print('public key')
	pkey = crypto.load_publickey(crypto.FILETYPE_PEM, public_key_in_text)
	key = pkey.to_cryptography_key()

	assert isinstance(key, rsa.RSAPublicKey)
	assert pkey.bits() == key.key_size
	
	print(pkey.bits())
	
	print('private key')
	pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, private_key_in_text)
	key = pkey.to_cryptography_key()

	assert isinstance(key, rsa.RSAPrivateKey)
	assert pkey.bits() == key.key_size
	
	print(pkey.bits())
	
	"""
	# encrypt with RSA 
	from Crypto.PublicKey import RSA
	from Crypto.Random import get_random_bytes
	from Crypto.Cipher import AES, PKCS1_OAEP
	from Crypto import Random
 
	number_of_bytes = 16
	# AES_MODE = AES.MODE_EAX
	AES_MODE = AES.MODE_CBC
	
	path_to_data = './data/message_payload/'
	message_payload_file = join(path_to_data, 'encrypted_data.bin')
	
	with open(message_payload_file, 'wb') as out_file:
		recipient_key = RSA.importKey(
			open(public_key_file_to_read_from).read())	
		session_key = get_random_bytes(number_of_bytes)
	
		cipher_rsa = PKCS1_OAEP.new(recipient_key)
		out_file.write(cipher_rsa.encrypt(session_key))
		
		iv = Random.new().read(AES.block_size)
		cipher_aes = AES.new(session_key, AES_MODE, iv)
		data_message_payload = b'Walnuss crossing the Technological Era'
		data_message_payload = _pad(data_message_payload)
		ciphertext = base64.b64encode(iv + cipher.encrypt(data_message_payload))
	
		out_file.write(ciphertext)
	
	# decrypt with RSA 
	passcode = ''
 
	with open(message_payload_file, 'rb') as fobj:
		private_key = RSA.importKey(
			open(private_key_file_to_read_from).read(),
			passphrase=passcode)
	
		enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
													for x in (private_key.size_in_bytes(), 
													number_of_bytes, number_of_bytes, -1) ]
	
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)
		
		ciphertext = base64.b64decode(ciphertext)
		iv = ciphertext[:AES.block_size]
		cipher = AES.new(self.key, AES.MODE_CBC, iv)

		data_message_payload_deciphered = cipher_aes.decrypt_and_verify(_unpad(cipher.decrypt(ciphertext[AES.block_size:])).decode('utf-8'), tag)
	
	print(data_message_payload_deciphered)
	"""
	
	declare_object_end('certificate_generator')
	declare_object_end('display_console')	
	"""
	openssl x509 -in ./data/certificates/trial/CA.crt -text -noout
	openssl rsa -in ./data/certificates/trial/CA.private.key -check

	
	Ref: https://github.com/pyca/pyopenssl/blob/master/examples/mk_simple_certs.py
	
	# pem to crt
	openssl x509 -outform der -in *.pem -out *.crt
	
	from cryptography import x509
	>>> from cryptography.hazmat.backends import default_backend
	>>> cert = x509.load_pem_x509_certificate(pem_data, default_backend())
	>>> cert.serial_number
	import subprocess
	cert_txt = subprocess.check_output(["openssl", "x509", "-text", "-noout", 
										"-in", certificate])
	from pyasn1_modules import pem, rfc2459
	from pyasn1.codec.der import decoder
	
	substrate = pem.readPemFromFile(open('cert.pem'))
	cert = decoder.decode(substrate, asn1Spec=rfc2459.Certificate())[0]
	print(cert.prettyPrint())
	#
	with open(certificate_file_chosen, "rb") as f:
		der = f.read()
	
	import OpenSSL.crypto
	
	x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, der)
	pkey = x509.get_pubkey()
	dir(pkey)
	['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'bits', 'check', 'generate_key', 'type']
	pkey.bits()
	4096L
	pkey.type() == OpenSSL.crypto.TYPE_RSA
	
	cert2 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, public_key)
	pkey = cert2.get_pubkey()
	
	print(dir(pkey))
	print(pkey.bits())
	
	print(pkey.type() == OpenSSL.crypto.TYPE_RSA)
	"""
	
	'''
	cat rsa.public.pem
	cat rsa.private.pem
	
	'''
		
	