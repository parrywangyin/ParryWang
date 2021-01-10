import threading
import time

def do_something():
    time.sleep(1)

start_time = time.perf_counter()
#创建threads空列表，用for循环创建10个线程,将它们一一全部放入threads列表中，然后再遍历threads列表，对里面所有的线程一一使用join()
threads = []

for i in range(1,11):
    t = threading.Thread(target=do_something, name=f'线程{str(i)}')
    print (f'{t.name}开始运行')
    print ('休眠1秒')
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time, 2)}秒')
