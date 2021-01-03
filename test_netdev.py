import asyncio
import netdev
import time
  
async def task(dev):
  async with netdev.create(**dev) as ios:
    out = await ios.send_command('show ip int b')
    print(out)
  
async def run():
  devices = []
  f = open('ip_list.txt')
  for ips in f.readlines():
    ip = ips.strip()
    dev = { 'username' : 'parry',
    'password' : 'afmo9se8e!',
    'device_type': 'cisco_ios',
    'host': ip
    }
    devices.append(dev)
  tasks = [task(dev) for dev in devices]
  await asyncio.wait(tasks)
  
start_time = time.time()
asyncio.run(run())
print ('Time elapsed: %.2f'%(time.time()-start_time))
