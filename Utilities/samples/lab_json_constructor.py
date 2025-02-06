import random
import json

import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/time')
sys.path.append(lib_path)

# import package from path
from timer_0 import timer_0 as timer	# file name
# from timer import timer	# file name

def random_select(list_target):
    candidate_selected = random.choice(list_target)
    return candidate_selected

data = {}

number_of_keys = 10

key_list, value_list = [], []
"""
for i in range(0, number_of_keys):
    if i < 10:
        index = '0' + str(i)
    else:
        index = str(i)

    key_list.append('key_' + index)
    value_list.append('value_' + index)
"""

id_timer = "Test Usage Agent: < timer >"
print("=====[" + id_timer + " Start]===== \n")
timer_object = timer(id_timer)

fields = ['accounts_entities', 'conditions_policy_of_use', 'enrollment_means', 'conditions_policy_of_residency', \
          'cryptographic_profile', 'key_usage', 'resources_permissible', 'account_DL', 'duration_of_permit']
accounts_entities = ['service', 'user', 'device']
conditions_policy_of_use = ['type_00', 'type_01', 'type_02', 'type_03']

enrollment_means = ['automated', 'manual']
conditions_policy_of_residency = [ 'active domain', 'zone_A', 'zone_B']
cryptographic_profile = ['ecdhe2048_rsa2048_aes256_gcm_sha384', 'ecdhe2048-rsa2048-chacha20-poly1305']
key_usage = ['Digital_Signature_verification', 'Certificate Signing and verification', 'Code signing', 'CRL signing', 'Non-Repudiation_contentCommitment', 'Key Encipherment', 'Data Encipherment', 'Key Agreement']
resources_permissible = ['*keys', '*data', 'access_to_computational_resources / network']
account_DL = ['ursa@o.com', 'ursa@w.com', 'ursa@e.com'] # needs sign-over when hand-over

date_start = timer_object.generate_timestamp(2015, 9, 1, 0, 1, 1)
date_end = timer_object.get_timestamp()
valid_time_epoch = date_start + ' to ' + date_end
duration_of_permit = [valid_time_epoch]

given_lists = [accounts_entities, conditions_policy_of_use, enrollment_means, conditions_policy_of_residency, \
          cryptographic_profile, key_usage, resources_permissible, account_DL, duration_of_permit]

number_of_keys = len(fields)

for i in range(0, number_of_keys):
    key_list.append(fields[i])


for i in range(0, number_of_keys):
    value_list.append(random_select(given_lists[i]))

for i in range(0, number_of_keys):
    data[key_list[i]] = value_list[i]


"""
data_parsed = json.loads(data)
json_data = json.dumps(data_parsed, indent=4, sort_keys=True) 
"""
json_data = json.dumps(data, indent=4, sort_keys=True)

print(json_data)
