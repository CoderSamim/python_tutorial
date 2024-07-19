#creating thread by inheritance process
from threading import Thread

#threading is module(file) name and Thread is a class under threading module

class MyThread(Thread):
    def run(self):     #method override
        for i in range(2000):
            print(i)

t1=MyThread()    #t1 is object of MyThread class

t1.start()

t1.join()  #wait for the completion of the thread   #optional



