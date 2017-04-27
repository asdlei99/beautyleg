#coding-utf-8
import os

basepath = "D:\\MY_DownLoad\\"
url = "http://www.beautylegmm.com/photo/beautyleg/2017/1438/beautyleg-1438-0058.jpg"

class AxelDownLoader(object):

    def __init__(self, link, path=''):
        self.link = link
        self.path = os.path.join(basepath, path)
        if not os.path.isdir(self.path):
            print("will add new file fold "+self.path)  
            os.mkdir(self.path)
        
    def setLink(self,link):
        self.link = link
        return self
    
    def getLink(self):
        return self.link

    def setPath(self,path):
        self.path = os.path.join(basepath, path)
        if not os.path.isdir(self.path):
            print("will add new file fold"+self.path)  
            os.mkdir(self.path)
        return self
    
    def getPath(self):
        return self.path   
        
    def downLoadLink(self):
        print(self.link)
        os.system("D:\\Axel_v2.5\\axel.exe -n 5 -a -S5 "+self.link+" -o "+self.path)    
        
if __name__=="__main__":
    print('runing..............')
    a = AxelDownLoader(url)
    a.downLoadLink()
    print('done')         

