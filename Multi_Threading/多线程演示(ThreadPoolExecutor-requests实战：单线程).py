import concurrent.futures
import time
import requests

urls = [
'https://images.unsplash.com/photo-1593501419344-82be41c9c1b1',
]

start_time = time.perf_counter()

for url in urls:
    img_bytes = requests.get(url).content
    img_name = url.split('/')[3] + '.jpg'
    with open (img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print (f'正在下载{img_name}')
    
end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')