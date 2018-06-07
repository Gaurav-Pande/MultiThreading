# a basic timer program which outputs time after a  certain interval of time
# Thread usually run along the main thread and shares the common memory
# Even though the execution of the main program ends, the thread continues to run


from threading import Thread
import time

def timer(name,delay,repeat):
    print ("timer has started at time !!" + str(time.ctime(time.time())))
    while repeat > 0:
        print (name + " is going to wait for " + str(delay) + " secs!!")
        time.sleep(delay)
        print (name + ":" +str(time.ctime(time.time())))
        repeat -= 1
    print(name + " is completed!!")


def Main():
    t1 = Thread(target=timer, args= ("timer1", 10 ,5))
    t2 = Thread(target=timer,args= ("timer2",5, 1))
    t1.start()
    t2.start()
    print ("main function completed its execution!!!")

if __name__ == "__main__":
    Main()