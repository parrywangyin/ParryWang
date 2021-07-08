import os 
import asyncio
import time
import subprocess
import re

if os.path.exists('ip_list.txt'):
    os.remove('ip_list.txt')

async def ping(last_octect):
	for third_octect in range(200,225):
		ip = '172.16.%s.%s' % (str(third_octect), str(last_octect))
		#打印出来让人看到异步是怎么ping的
		#print ('ping -n 1 -w 1 %s' % ip)
		proc = await asyncio.create_subprocess_exec('ping', '-n', '1','-w','1', ip, stdout=asyncio.subprocess.PIPE)
		ping_result = await proc.stdout.read()
		#看到执行ping命令后的回显内容，可以通过正则表达式来匹配100% loss的关键字
		print (ping_result.decode('utf-8'))
		ping_result_decider = re.search('Received = 1', ping_result.decode('utf-8'))
		if ping_result_decider:
			print (ip + ' is reachable.')
			#f = open('C:\\port\\reachable_ip.txt','a+')
			f = open('ip_list.txt', 'a+')
			f.write(ip + '\n')
		else:
			print (ip + ' is not reachable.')

async def main():
	tasks = []
	for i in range(1,255):
		tasks.append(ping(i))
	await asyncio.wait(tasks)
loop = asyncio.ProactorEventLoop()
asyncio.set_event_loop(loop)
start_time = time.time()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
print ('Time elapsed: %.2f'%(time.time()-start_time))