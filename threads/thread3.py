#pass argument
from threading import *


def display(str):
    print(str)


for i in range(5):
    t = Thread(target=display,args=('[RUNNING] running.....',))

    t.start()
