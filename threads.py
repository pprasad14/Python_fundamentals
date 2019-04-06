import threading

def print_square(num):
    print("Square : {}".format(num*num))
    
def print_cube(num):
    print("Cube: {}".format(num*num*num))

if __name__ == '__main__':
    #creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(5,))
    
    #starting t1
    t1.start()
    #starting t2
    t2.start()
    
    #wait for t1 to complete
    t1.join()
    #wait for t2 to complete
    t2.join()
    
    #only when both threads are completed
    print("Done!")

################

import threading
import os

def task1():
    print("Task 1 assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running task 1 : {}".format(os.getpid()))
    
def task2():
    print("Task 2 assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running task 2 : {}".format(os.getpid()))
    
if __name__ == '__main__':
    print("ID of process running main program: {}".format(os.getpid()))
    
    print("Main thread name: {}".format(threading.main_thread().name))
    
    #creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    
    #starting threads
    t1.start()
    t2.start()
    
    #wait until thread complete execution
    t1.join()
    t2.join()
    
##################
#example of race condition
    
import threading

x = 0

def increment():
    global x
    x += 1
    
def thread_task():
    for _ in range(100000):
        increment()
    
def main_task():
    
    global x
    x = 0
    
    #creating threads
    t1 = threading.Thread(target = thread_task)
    t2 = threading.Thread(target = thread_task)
    
    #starting threads
    t1.start()
    t2.start()
    
    #waiting till finish of both threads
    t1.join()
    t2.join()
    
if __name__ == '__main__':
    
    for i in range(10):
        main_task()
        print("Iteration {} : x is {}".format(i,x))
    
##############
#uisng lock for above example

import threading

x = 0

def increment():
    global x
    x += 1
    
def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()
    
def main_task():
    
    global x
    x = 0

    #creating lock
    lock = threading.Lock()
    
    #creating threads
    t1 = threading.Thread(target = thread_task, args=(lock,))
    t2 = threading.Thread(target = thread_task, args=(lock,))
    
    #starting threads
    t1.start()
    t2.start()
    
    #waiting till finish of both threads
    t1.join()
    t2.join()
    
if __name__ == '__main__':
    
    for i in range(10):
        main_task()
        print("Iteration {} : x is {}".format(i,x))
            
        
#################
#testing
        
import threading
count_t1 = 0
count_t2 = 0

x = 0

def increment():
    global x
    x += 1
    
def thread_task():
    global count_t1, count_t2
    
    for _ in range(100000):
        if threading.current_thread().name == 't1':
            count_t1 += 1
        if threading.current_thread().name == 't2':
            count_t2 += 1
        increment()
    
def main_task():
    
    global x
    x = 0
    
    #creating threads
    t1 = threading.Thread(target = thread_task, name = 't1')
    t2 = threading.Thread(target = thread_task, name = 't2')
    
    #starting threads
    t1.start()
    t2.start()
    
    #waiting till finish of both threads
    t1.join()
    t2.join()
    
if __name__ == '__main__':
    
    for i in range(10):
        main_task()
        print("Iteration {} : x is {}".format(i,x))
    
    print("Count of t1: ",count_t1)
    print("Count of t2: ",count_t2)
    