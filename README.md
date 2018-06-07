# MultiThreading
Learning multithreading in a pythonic way


## Notes compiled from various sources:


In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process!

A thread contains all this information in a Thread Control Block (TCB):
A program can be treated as a process and all its information is stored in Process control Block(PCB)

* Thread Identifier: Unique id (TID) is assigned to every new thread

* Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.

* Program counter: a register which stores the address of the instruction currently being executed by thread.

* Thread state: can be running, ready, waiting, start or done.

* Thread’s register set: registers assigned to thread for computations.

* Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.


![Image](https://github.com/Gaurav-Pande/MultiThreading/blob/master/assets/2.png)


In a simple, single-core CPU, it is achieved using frequent switching between threads. This is termed as context switching. In context switching, the state of a thread is saved and state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place. Context switching takes place so frequently that all the threads appear to be running parallely (this is termed as multitasking).




### Important points to remember by

![Image1](https://github.com/Gaurav-Pande/MultiThreading/blob/master/assets/1.png)


* As you can see in the diagram threads share the common global varaible data.

![Image2](https://github.com/Gaurav-Pande/MultiThreading/blob/master/assets/4.png)


* In a cpu of single core, threading is achieved by context switching.

* Multithreading is actually does not means running threads in parallel in python. This does not happen due to GIL or Global Interpreter Lock, due to which only a single thread is executed at a time by cpu. It means that, if you have 8 threads and if you try to run them in a 8 core cpu, than your processor will still utilize 100% cpu rather than using 800% cpu.

* But still the threading will make execution faster. How??  It is due to the fact that all process are not cpu intensive process, for example: if you are downloading hundreds of images from internet than most of the time is spend in IO process which is connecting to internet server, than downloading etc. So using threads what will happen is while an image is getting downloaded from internet our cpu can run another thread as at this point of time, cpu is idle. 

* More importantly, there are cases where this doesn't matter. For example, a network server spends most of its time reading packets off the network, and a GUI app spends most of its time waiting for user events. One reason to use threads in a network server or GUI app is to allow you to do long-running "background tasks" without stopping the main thread from continuing to service network packets or GUI events. And that works just fine with Python threads. (In technical terms, this means Python threads give you concurrency, even though they don't give you core-parallelism.)

* So, the crux is if your program is IO oriented than use multithreading and it is efficient, but if it is an CPU intensive process like bitcoin mining, zipping a file than multithreadint will not be a good option.

### Synchronization


Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section.

* Critical section refers to the parts of the program where the shared resource is accessed.

* Concurrent accesses to shared resource can lead to race condition. Meaning if multiple threads tries to access the same variable than there might be unpredictable changes in the value of the variable.

* Synchronization in python is done using locks(threading.lock). The mechanism behind the implementation of the locks is done using semaphores which is an object provided by the OS (in lay man terms, os assigns a value say 0 or 1 to the critical section, and if a thread wants to access this critical section thant the thread will access via this value and while exiting from the critical section it revert back the value to its original so that other thread can access it. this is similar like booking using token)

*A semaphore is a synchronization object that controls access by multiple processes/threads to a common resource in a parallel programming environment. It is simply a value in a designated place in operating system (or kernel) storage that each process/thread can check and then change. Depending on the value that is found, the process/thread can use the resource or will find that it is already in use and must wait for some period before trying again. Semaphores can be binary (0 or 1) or can have additional values. Typically, a process/thread using semaphores checks the value and then, if it using the resource, changes the value to reflect this so that subsequent semaphore users will know to wait





### Some links to visits:

https://www.geeksforgeeks.org/multithreading-python-set-1/

https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

https://stackoverflow.com/questions/18114285/what-are-the-differences-between-the-threading-and-multiprocessing-modules/18114882#18114882

https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/


