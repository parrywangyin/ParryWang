import concurrent.futures
import time

def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return 'test'

start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    #用list comprehension创建10个future objects并运行，到这里10个并发任务就完成了，下面调用results()的代码为可选内容
    results = [executor.submit(do_something, 1) for _ in range(10)]
    #用as_completed来遍历所有的futures，并用result()打印出每个任务返回的结果
    for f in concurrent.futures.as_completed(results):
        print (f.result())

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')
