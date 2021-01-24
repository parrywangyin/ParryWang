from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
targets = nr.filter(building='1')
results = sw4.run(netmiko_send_command, command_string='sh ip arp')

print_result(results)

