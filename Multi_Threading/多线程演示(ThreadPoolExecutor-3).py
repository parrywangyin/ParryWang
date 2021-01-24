import concurrent.futures
import time

def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return 'test'

start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    #用list comprehension来遍历seconds列表里的元素，总共5次并发执行do_something()后，每次的休眠时间分别从5秒，4秒...再到1秒。
    seconds = [5,4,3,2,1]
    results = [executor.submit(do_something, second) for second in seconds]
    #用as_completed来遍历所有的futures，并用result()打印出每个任务返回的结果
    for f in concurrent.futures.as_completed(results):
        print (f.result())

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')