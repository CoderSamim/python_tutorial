#check what is the current thread
import threading

print('let us find the current thread')

print(threading.current_thread())  #here we get thread name with other information


print(threading.current_thread().getName())  #current thread is main, here we get only the name of thread


#checking if it is main thred or not?

if threading.current_thread()==threading.main_thread():
    print('it is main thread')
else:
    print('not main thread')





