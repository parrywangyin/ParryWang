import time
import requests
import concurrent.futures

urls = [
'https://images.unsplash.com/photo-1593501419344-82be41c9c1b1',
'https://images.unsplash.com/photo-1546299428-1d800272dc97',
'https://images.unsplash.com/photo-1609645778471-613f21fcf3df',
'https://images.unsplash.com/photo-1608915939262-337b9724f65d',
'https://images.unsplash.com/photo-1603561943596-be37143927ec',
'https://images.unsplash.com/photo-1606247919215-3ce82d2e45d8',
'https://images.unsplash.com/photo-1594842084112-fe6d71906449',
'https://images.unsplash.com/photo-1573592234083-c0b2fbda21bb'
]
start_time = time.perf_counter()

#这里定义一个函数来下载一个图片，函数后面的参数名可以任意取名，不一定必须是(url)，用(abc)也是一样的
def download_img(url):
    img_bytes = requests.get(url).content
    img_name = url.split('/')[3] + '.jpg'
    with open (img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print (f'正在下载{img_name}')

#用ThreadPoolExecutor配合map()遍历列表urls里的内容，并且将其中每个元素，也就是每张图片的url并发下载。
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, urls)

end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')