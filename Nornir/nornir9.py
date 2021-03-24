from nornir import InitNornir
from nornir_scrapli.tasks import get_prompt, send_command, send_configs

nr = InitNornir(config_file="config.yaml")

prompt_results = nr.run(task=get_prompt)
config_results = nr.run(task=send_configs, configs=["interface loop99", "description Nornir loopback"])
command_results = nr.run(task=send_command, command="wr mem")

print(prompt_results["sw1"].result)
print(config_results["sw1"].result)
print(command_results["sw1"].result)
