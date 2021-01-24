from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
#sw4 = nr.filter(filter_func=lambda host: host.name== 'sw4')
switches = ['192.168.2.11','192.168.2.12','192.168.2.13']
sw1_sw2_sw3 = nr.filter(filter_func=lambda host: host.hostname in switches)

results = sw1_sw2_sw3.run(netmiko_send_command, command_string='sh ip arp')

print_result(results)

