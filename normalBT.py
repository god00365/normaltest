import urllib2
import requests
import time
from time import sleep


#proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:80"})
#opener = urllib2.build_opener(proxy_support) 

text = open("normalBT.txt",'a')


for i in range(0, 5):


    
    #urllib2.install_opener(opener)
    

    urls = ['http://google.com','http://facebook.com','http://youtube.com/','http://yahoo.com','http://baidu.com/','http://qq.com','http://live.com','http://cnn.com/','http://espn.go.com/','http://taobao.com/','http://linkedin.com/','http://sina.com.cn','http://twitter.com','http://amazon.com/','http://hao123.com','http://stackoverflow.com','http://blogspot.com','http://weibo.com/','http://163.com','http://wordpress.com','http://livedoor.com','http://bing.com/','http://360.cn','http://yandex.ru','http://vk.com','http://ebay.com','http://google.de/','http://babylon.com','http://msn.com','http://google.co.uk','http://soso.com/','http://avg.com','http://tumblr.com/','http://google.co.uk','http://mail.ru','http://pinterest.com','http://google.co.jp','http://apple.com','http://microsoft.com','http://PayPal.com','http://blogger.com','http://fc2.com/','http://blogger.com','http://imdb.com/','http://craigslist.org','http://ask.com/','http://sohu.com/','http://conduit.com','http://bbc.co.uk/','http://go.com/']

    for urllist in range(0, 50):

	connect  = requests.get(urls[urllist])
	
	connect.connection.close()
	sleep(1)

    start = time.time()

    request = urllib2.Request("http://en.wikipedia.org/wiki/Main_Page")
    
    request.add_header('Pragma','no-store,no-cache,must-revalidate')
    request.add_header('Cache-Control', 'no-cache')
    
    
    content = urllib2.build_opener().open(request).read()

    end = time.time()
    result = end - start
    
    text.write("%s\n" % (result))
    #time.sleep(1)

