import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')
#ipdb.set_trace()
print (nr.inventory.hosts['sw1'].name)
print (nr.inventory.hosts['sw1'].hostname)
print (nr.inventory.hosts['sw1'].username)
print (nr.inventory.hosts['sw1'].password)
print (nr.inventory.hosts['sw1'].platform)
print (nr.inventory.hosts['sw1'].groups)
print (nr.inventory.hosts['sw1'].data)
