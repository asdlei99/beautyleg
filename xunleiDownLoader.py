# -*- coding=utf-8 -*- 
import os 
import time 
from win32com.client import Dispatch 
import inspect

def addTasktoXunlei(down_url,fileName): 
    flag = False 
    o = Dispatch("ThunderAgent.Agent64.1") 
    try: 
		#迅雷9.1.30无法指定文件夹,原因未知
        o.AddTask(down_url, fileName, "", "", "", -1, 0, 5) 
        o.CommitTasks() 
        flag = True 
    except Exception: 
        print(Exception.message) 
        print(" AddTask is fail!") 
    return flag 
    
    
if __name__=="__main__":
    print('runing..............')
    addTasktoXunlei('http://wvw.rosmm.com/pic/upload/2017/04/24/rosmm-1965-1.jpg', '1.jpg')
    print('done')       

