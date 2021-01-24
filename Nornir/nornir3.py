from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
group1 = nr.filter(F(groups__contains="cisco_group1"))
group2 = nr.filter(~F(groups__contains="cisco_group1"))
results = nr.run(netmiko_send_command, command_string='sh ip int brief') 

print_result(results)
