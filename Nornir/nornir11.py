import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
output = nr.run(netmiko_send_command, command_string='sh interface switchport', use_textfsm=True)
#print_result(output)
#print(output)
#ipdb.set_trace()
print (output['sw1'].result[0]['mode'])

