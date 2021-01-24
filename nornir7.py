from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date
import pathlib

def backup_configurations(task):
    r = task.run(task=napalm_get, getters=["config"])
    task.run(task=write_file, content=r.result["config"]["running"], filename=str(task.host.name) + "-" + str(date.today()) + ".txt")


nr = InitNornir(config_file="config.yaml")
result = nr.run(name="正在备份交换机配置", task=backup_configurations)

print_result(result)
