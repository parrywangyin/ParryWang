import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
#from nornir.core.task import Task, Result

def hello_world(task):
    r = task.run(netmiko_send_command, command_string='show interface switchport', use_textfsm=True)
    task.host['facts'] = r.result #写成task.host.data['facts']也可以，data是一组字典

nr = InitNornir(config_file='config.yaml')
result = nr.run(task=hello_world)
print_result(result)
ipdb.set_trace()
