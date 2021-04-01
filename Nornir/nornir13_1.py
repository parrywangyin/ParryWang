#这篇实验讲解Nornir中Task的用法，task就是Python中的一种函数，该函数包含一个参数task，返回的结果为一个Result数据类型。
#这篇注意函数下面的task.host.xxxx（对应的hosts.yaml下每台设备的属性）不能在ipdb里调用，因为没有对应的变量，可以用nr.inventory.hosts['swX'].xxxx替代。

import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
#from nornir.core.task import Task, Result

nr = InitNornir(config_file='config.yaml')
def hello_world(task):
    return (task.host.name, #等同于在ipdb里面输入nr.inventory.hosts['swX'].name
    	task.host.hostname, #等同于在ipdb里面输入nr.inventory.hosts['swX'].hostname
    	task.host.username, #等同于在ipdb里面输入nr.inventory.hosts['swX'].username
    	task.host.password, #等同于在ipdb里面输入nr.inventory.hosts['swX'].password
    	task.host.platform, #等同于在ipdb里面输入nr.inventory.hosts['swX'].platform
    	task.host.groups #groups是列表, 等同于在ipdb里面输入nr.inventory.hosts['swX'].groups
    	task.host.data) #data是字典, 等同于在ipdb里面输入nr.inventory.hosts['swX'].data

result = nr.run(task=hello_world)
print_result(result)
ipdb.set_trace()
