#creating thread, by create object of Thread class
from threading import *

def display():
    print('[RUNNING] running.....')

for i in range(5):
    #t=Thread(display())  #t is a object of thread class
    #here t is a thread for display function

    t = Thread(target=display)

    t.start()     #to start the thread t , call start()



