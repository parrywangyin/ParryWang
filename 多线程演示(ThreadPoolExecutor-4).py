import concurrent.futures
import time

def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return 'test'

start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    #用map()函数来代替list comprehension
    sec = [5,4,3,2,1]
    results = executor.map(do_something, sec)
    #打印出最后的'test'，这步可以省去
    for result in results:
        print (result)

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')

