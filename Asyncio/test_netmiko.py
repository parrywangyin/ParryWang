from netmiko import ConnectHandler
import time
  
f = open('ip_list.txt')
start_time = time.time()

for ips in f.readlines():
  ip = ips.strip()
  device = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': 'parry',
    'password': 'afmo9se8e!'
  }
  ssh_client = ConnectHandler(**device)
  output = ssh_client.send_command('show ip int b')
  print (output)

print ('Time elapsed: %.2f'%(time.time()-start_time))
