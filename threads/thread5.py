#use instance variable
from threading import Thread


class MyThread(Thread):
    #def __init__(self,str):
        #self.str=str

    def __init__(self,str):
        Thread.__init__(self)   #to use with Thread class __init__method also #avoid override
        self.str=str


    def run(self):
            print(self.str)

t1=MyThread('[RUNNING] running.....')

t1.start()

t1.join()



