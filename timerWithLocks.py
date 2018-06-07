# a basic timer program which outputs time after a  certain interval of time
# Thread usually run along the main thread and shares the common memory
# Even though the execution of the main program ends, the thread continues to run
# here we define a lock and each thread acquire a lock and executes the thread and
# the other thread waits until the first thread completes its execution
# lock is implemented for synchronization
# And lock functionality is implemented in python using semaphores

import threading
import time

lock1 = threading.Lock()

def timer(name,delay,repeat):
    print ("timer has started at time !!" + str(time.ctime(time.time())))
    lock1.acquire()
    print (name + ":" + "has acquired the lock~~")
    while repeat > 0:
        print (name + " is going to wait for " + str(delay) + " secs!!")
        time.sleep(delay)
        print (name + ":" +str(time.ctime(time.time())))
        repeat -= 1
    lock1.release()
    print(name + ":" + "has released the lock~~")
    print(name + " is completed!!")


def Main():
    t1 = threading.Thread(target=timer, args= ("timer1", 10 ,5))
    t2 = threading.Thread(target=timer,args= ("timer2",5, 1))
    t1.start()
    t2.start()
    print ("main function completed its execution!!!")

if __name__ == "__main__":
    Main()