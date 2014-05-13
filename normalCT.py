import requests
import re
import time
from multiprocessing import Process, Pool
import urllib2
from time import sleep

text = open("normalCT.txt",'a')

def http_get(image):
	
	#result = {"url": image, "data": requests.get(image, headers=headers)}
	result = requests.get(image, headers=headers)
	result.connection.close()
	sleep(1)
	return result




for i in range(0, 5):

	start1 = time.time()



        urls = ['http://google.com','http://facebook.com','http://youtube.com/','http://yahoo.com','http://baidu.com/','http://qq.com','http://live.com','http://cnn.com/','http://espn.go.com/','http://taobao.com/','http://linkedin.com/','http://sina.com.cn','http://twitter.com','http://amazon.com/','http://hao123.com','http://stackoverflow.com','http://blogspot.com','http://weibo.com/','http://163.com','http://wordpress.com','http://livedoor.com','http://bing.com/','http://360.cn','http://yandex.ru','http://vk.com','http://ebay.com','http://google.de/','http://babylon.com','http://msn.com','http://google.co.uk','http://soso.com/','http://avg.com','http://tumblr.com/','http://google.co.uk','http://mail.ru','http://pinterest.com','http://google.co.jp','http://apple.com','http://microsoft.com','http://PayPal.com','http://blogger.com','http://fc2.com/','http://blogger.com','http://imdb.com/','http://craigslist.org','http://ask.com/','http://sohu.com/','http://conduit.com','http://bbc.co.uk/','http://go.com/']

#        for urllist in range(0, 50):
#
#	     connect  = requests.get(urls[urllist])
#	
#	     connect.connection.close()
#	     sleep(1)


	headers = {'cache-control':'no-cache'}
	website = requests.get('http://en.wikipedia.org/wiki/Main_Page', headers=headers)
	
	html = website.text
	pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
	img = pat.findall(html)

	imglen = len(img)

	for num in range(0,imglen) :
		img[num] = 'http:'+img[num]

	
	
	opener = urllib2.build_opener() 
	

	pool = Pool(processes = imglen)

	results = pool.map(http_get, img)
	
	end2 = time.time()

	
	res = end2 - start1
	
	text.write("%s\n" % (res))
	

	
