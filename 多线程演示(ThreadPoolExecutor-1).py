import concurrent.futures
import time

def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return 'test'

start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1) #submit()函数返回一个future object,通过它主线程(或进程)可以获取某一个线程(进程)执行的状态或者某一个任务执行的状态及返回值
    f2 = executor.submit(do_something, 1) #submit()函数返回一个future object,通过它主线程(或进程)可以获取某一个线程(进程)执行的状态或者某一个任务执行的状态及返回值
    print (f1.result()) #result()返回的是do_something()下面return的内容，也就是这里的'test'
    print (f2.result()) #result()返回的是do_something()下面return的内容，也就是这里的'test'
    print (f'task1是否完成: {f1.done()}')#done()返回的是布尔值，用来判断任务（也就是do_something()函数)是否运行完成
    print (f'task2是否完成: {f1.done()}')#done()返回的是布尔值，用来判断任务（也就是do_something()函数)是否运行完成

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')
