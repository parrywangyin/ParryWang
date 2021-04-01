#这篇注意hosts.yaml下的groups为列表，data为字典。

import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
#from nornir.core.task import Task, Result

nr = InitNornir(config_file='config.yaml')
def hello_world(task):
    return (task.host.groups[0], 
            task.host.data['building'],#只能读取data下面的键名(building或者level),因为data是一个字典，不能写作task.host['data']，只能写成task.host.data
            task.host['building'])#也可以把task.host.data['building']写成task.host['building']

result = nr.run(task=hello_world)
print_result(result)
ipdb.set_trace()
