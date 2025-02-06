"""
Certificate generation module.
"""
from OpenSSL import crypto, SSL
from cryptography.hazmat.primitives.asymmetric import rsa

from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join

TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA

import os, sys
lib_path = os.path.abspath('../../../../Libraries/display/console')
sys.path.append(lib_path)

from display_console import display_console	


def initialize_object (object_type, object_ID):
	id_object = "Test Usage Agent: <" + object_ID + ">"
	print ("=====[" + id_object + " Start]===== \n")
	object = object_type(id_object)
	
	return object
	
def declare_object_end (object_ID):
	print ("=====[" + object_ID + " End]=====")

class certificate_generator:
	display_console_object = '';

	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);
		self.display_console_object = initialize_object (display_console, 'display_console')
		
	def create_key_pair(self, type, bits):
		"""
		Create a public/private key pair.
	
		Arguments: type - Key type, must be one of TYPE_RSA and TYPE_DSA
				bits - Number of bits to use in the key
		Returns:   The public/private key pair in a PKey object
		"""
		pkey = crypto.PKey()
		pkey.generate_key(type, bits)
		return pkey
	
	
	def create_certificate_request(self, pkey, digest="sha256", **name):
		"""
		Create a certificate request.
	
		Arguments: pkey   - The key to associate with the request
				digest - Digestion method to use for signing, default is sha256
				**name - The name of the subject of the request, possible
							arguments are:
							C     - Country name
							ST    - State or province name
							L     - Locality name
							O     - Organization name
							OU    - Organizational unit name
							CN    - Common name
							emailAddress - E-mail address
		Returns:   The certificate request in an X509Req object
		"""
		req = crypto.X509Req()
		subj = req.get_subject()
	
		print(type(name))
		for key, value in name.items():
			setattr(subj, key, value)
	
		req.set_pubkey(pkey)
		req.sign(pkey, digest)
		return req
	
	
	def create_certificate(self, req, issuerCertKey, serial, validityPeriod, 
						digest="sha256"):
		"""
		Generate a certificate given a certificate request.
	
		Arguments: req        - Certificate request to use
				issuerCert - The certificate of the issuer
				issuerKey  - The private key of the issuer
				serial     - Serial number for the certificate
				notBefore  - Timestamp (relative to now) when the certificate
								starts being valid
				notAfter   - Timestamp (relative to now) when the certificate
								stops being valid
				digest     - Digest method to use for signing, default is sha256
		Returns:   The signed certificate in an X509 object
		"""
		issuerCert, issuerKey = issuerCertKey
		notBefore, notAfter = validityPeriod
		cert = crypto.X509()
		cert.set_serial_number(serial)
		cert.gmtime_adj_notBefore(notBefore)
		cert.gmtime_adj_notAfter(notAfter)
		cert.set_issuer(issuerCert.get_subject())
		cert.set_subject(req.get_subject())
		cert.set_pubkey(req.get_pubkey())
		cert.sign(issuerKey, digest)
		
		return cert
		
	def read_key_from_key_file (self,  key_file_to_read_from):
		with open(key_file_to_read_from, 'rb') as f:
			key_in_text = f.read()	
				
		if 'private'.upper() in str(key_in_text):
			print('private key')
			pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key_in_text)
			key = pkey.to_cryptography_key()
			
			'''
			passphrase = b"secret"
			called = []

			key = load_privatekey(FILETYPE_PEM, cleartextPrivateKeyPEM)
			pem = dump_privatekey(FILETYPE_PEM, key, CIPHER_ALGO, passphrase)
			assert isinstance(pem, binary_type)

			loadedKey = load_privatekey(FILETYPE_PEM, pem, passphrase)
			'''
			
			assert isinstance(key, rsa.RSAPrivateKey)
			# assert pkey.bits() == key.key_size
	
			print(pkey.bits())
				
		else:
			print('public key')
			pkey = crypto.load_publickey(crypto.FILETYPE_PEM, key_in_text)
			key = pkey.to_cryptography_key()
			
			assert isinstance(key, rsa.RSAPublicKey)
			# assert pkey.bits() == key.key_size
	
			print(pkey.bits())
		
		return key_in_text		
		
	def write_private_to_key_file (self, private_key, private_key_file_to_write_to):
		with open(private_key_file_to_write_to, 'wb') as f:
			f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, private_key))	
	
		return None
	
	def write_public_to_key_file (self, private_key, public_key_file_to_write_to):
		
		with open(public_key_file_to_write_to, 'wb') as f:
			f.write(crypto.dump_publickey(crypto.FILETYPE_PEM, private_key))
			
		return None	
	
	def write_certificate_to_certificate_file (self, certificate, certificate_file_to_write_to):
		with open(certificate_file_to_write_to, 'wb') as f:
			f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificate))
	
		return None	
		
	def get_certificate_profile (self, certificate_file, file_type):
		
		with open(certificate_file, "rb") as f:
			der_cert_file = f.read()
		
		if (file_type == crypto.FILETYPE_ASN1):
			x509_cert = crypto.load_certificate(crypto.FILETYPE_ASN1, der_cert_file)
		elif (file_type == crypto.FILETYPE_PEM):
			x509_cert = crypto.load_certificate(crypto.FILETYPE_PEM, der_cert_file)
		else:	# FILETYPE_TEXT
			# x509_cert = crypto.load_certificate(crypto.FILETYPE_TEXT, der_cert_file)
			raise ValueError("type argument must be FILETYPE_PEM or FILETYPE_ASN1")
		
		public_key = x509_cert.get_pubkey()
		
		print(dir(public_key))
		
		key_bits_length = public_key.bits()
		self.display_console_object.display_variable('key_bits_length', key_bits_length)
		
		if (public_key.type() == crypto.TYPE_RSA):
			print('key type: RSA')
		elif (public_key.type() == crypto.TYPE_DSA):
			print('key type: DSA')
		else:
			print('key type: Unknown')
		content_in_text = crypto.dump_publickey(crypto.FILETYPE_PEM, public_key)
		self.display_console_object.display_variable ('content_in_text', content_in_text)
		
		cert_details_object = x509_cert.get_subject()
		
		print('======= Agent =======')
		[country, state, city, organization, org_unit, user_id, serial_number] = [cert_details_object.C, cert_details_object.ST, cert_details_object.L, cert_details_object.O, cert_details_object.OU, cert_details_object.CN, x509_cert.get_serial_number()] 
		
		self.display_console_object.display_variable_list(['country', 'state', 'city', 'organization', 'org_unit', 'user_id', 'serial_number'], [country, state, city, organization, org_unit, user_id, serial_number])
		
		print('======= CA =======')
		print(x509_cert.get_issuer().ST)
		[country, state, city, organization, org_unit, user_id, serial_number] = [x509_cert.get_issuer().C, x509_cert.get_issuer().ST, x509_cert.get_issuer().L, x509_cert.get_issuer().O, x509_cert.get_issuer().OU, x509_cert.get_issuer().CN, 'xxxxxxxxxxxxx'] 
		
		self.display_console_object.display_variable_list(['country', 'state', 'city', 'organization', 'org_unit', 'user_id', 'serial_number'], [country, state, city, organization, org_unit, user_id, serial_number])
		
		# ref: http://pyopenssl.sourceforge.net/pyOpenSSL.html/openssl-x509.html	
		
		return None	
		
	def generate_asymetric_key_and_generate_certificate (self, asymetric_key_type, key_integrity_algo, key_length):
		key = crypto.PKey()
		key.generate_key(asymetric_key_type, key_length)
		certificate_object = crypto.X509()	# make cert
		certificate_object.set_pubkey(key)
		certificate_object.sign(key, key_integrity_algo)
		public_key = certificate_object.get_pubkey()
		print(dir(public_key))
		print(public_key.bits())
	
		return certificate_object
		
	def get_public_key_from_certificate_object (self, certificate_object, certificate_file_type):
		public_key =  crypto.dump_certificate(certificate_file_type, certificate_object)
	
		return public_key	
		
		
	from OpenSSL import crypto, SSL
	from socket import gethostname
	from pprint import pprint
	from time import gmtime, mktime
	from os.path import exists, join
	import os
	
	
	def create_self_signed_certificate(self, path_to_certificates, asymetric_key_type, key_integrity_algo, certificate_file_to_write_to, private_key_file_to_write_to, public_key_file_to_write_to, key_length, country, state, city, organization, org_unit, service_id, serial_number, validityPeriod):
		notBefore, notAfter = validityPeriod
		
		"""
		If *.crt and *.key don't exist in path_to_certificates, create a new
		self-signed cert and keypair and write them into that directory.
		"""
		if not exists(join(path_to_certificates, certificate_file_to_write_to)) \
			or not exists(join(path_to_certificates, private_key_file_to_write_to)):
			
			if not exists(path_to_certificates):
				os.mkdir(path_to_certificates)
			
			# create a key pair
			private_key = crypto.PKey()
			private_key.generate_key(asymetric_key_type, key_length) # crypto.TYPE_RSA
	
			public_key = crypto.dump_publickey(crypto.FILETYPE_PEM, private_key)
	
			self.display_console_object.display_variable('public_key', public_key)
			
			# create a self-signed cert
			cert = crypto.X509()
			cert.get_subject().C = country
			cert.get_subject().ST = state
			cert.get_subject().L = city
			cert.get_subject().O = organization
			cert.get_subject().OU = org_unit
			cert.get_subject().CN = service_id
			cert.set_serial_number(serial_number)
			cert.gmtime_adj_notBefore(notBefore)
			cert.gmtime_adj_notAfter(notAfter)
			cert.set_issuer(cert.get_subject())
			cert.set_pubkey(private_key) # public_key_object would be extracted internally
			cert.sign(private_key, key_integrity_algo) # public_key_object would be extracted internally
	
			certificate_file_to_write_to = os.path.join(path_to_certificates, certificate_file_to_write_to)
			self.write_certificate_to_certificate_file ( cert, certificate_file_to_write_to)
				
			private_key_file_to_write_to = os.path.join(path_to_certificates, private_key_file_to_write_to)
				
			self.write_private_to_key_file ( private_key, private_key_file_to_write_to)	
			
			public_key_file_to_write_to = os.path.join(path_to_certificates, public_key_file_to_write_to)	
			
			self.write_public_to_key_file (private_key, public_key_file_to_write_to)
			
			"""
			open(join(path_to_certificates, certificate_file_to_write_to), "wt").write(
				crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
			open(join(path_to_certificates, private_key_file_to_write_to), "wt").write(
				crypto.dump_privatekey(crypto.FILETYPE_PEM, private_key))
			
			# ref: Alternatively, https://gist.github.com/toolness/3073310
			https://www.programcreek.com/python/example/64089/OpenSSL.crypto.PKey
			"""
		return None		
		
	def __del__(self):
		print ("_gaia object [%s] removed\n" % self.id);
		declare_object_end('display_console')
	
####################################
## main
####################################
if __name__ == "__main__":
	id = "Library Agent: Internal Agent <certificate_generator>"
	print ("=====[" + id + " Start]===== \n")
	certificate_generator_object = certificate_generator(id)
	certificate_generator_object.who_am_i()
	
	#import _Gaia._gaia
	#help(certificate_generator) # introspect	
	
	print ("=====[" + id + " End]===== \n");	