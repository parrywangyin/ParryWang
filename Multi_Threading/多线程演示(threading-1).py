import threading
import time

def do_something():
    print ('休眠1秒')
    time.sleep(1)

start_time = time.perf_counter()

#手动创建两个线程
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join()

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time, 2)}秒')
