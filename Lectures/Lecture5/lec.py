# import csv
# reader=csv.reaader(open('simplecsv'))
# mydict={
# }
# for column in reader:
#     mydict[column[0]] = {'age':column[1],'color':column[2]}
  
  
# f=open("simplecsv")
# ls=f.readlines()
# data=ls.split(',')
# print(data[0])

# try:
#     print(1/0)
# except:
#     print('Error')
# else:
#     print('Success')
# finally:
#     print('Done')

##################################################################

# import threading 
# import time
# def task1(num):
#     for i in range(num):
#         print('Task1')
#         time.sleep(1)
    
# def task2(num):
#     for i in range(num):
#         print('Task2')
#         time.sleep(1)
    
# if __name__ == '__main__':
#     t1=threading.Thread(target=task1,args=(10000,))
#     t2=threading.Thread(target=task2,args=(10000,))
    
#     t1.start()
#     t2.start()
#     while True:
#         print('Task main 0')
#         time.sleep(1)
        

##################################################################

from tkinter import *
window =Tk()
window2 =Tk()
window.title("mohamed")
window.geometry("500x500+350+150")
window.resizable(False,False)
window.configure(background='red')
window2.mainloop() 

# classwidget(window,)
Entry=Entry()

