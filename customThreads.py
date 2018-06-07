# we can make our own Thread subclass by overriding the super class thread
# A simple program which runs a thread in the background wait for the main program to end and than writes a message to a file
# This type of write is called async write because the thread runs in the background

import threading
import time
import random

class asynWrite(threading.Thread):
    def __init__(self,text,filename):
        threading.Thread.__init__(self)
        self.text = text
        self.filename = filename

    def run(self):
        with open(self.filename,'w') as f:
            f.write(self.text)
        time.sleep(2)
        print ("finished writing to the file")

def Main():
    background = asynWrite("hellow how are you dear!!","hello.txt")
    background.start()
    print ("we have started the thread to run in background")
    print ("lets do something here at the main program, lets run some math")
    for x in range(10):
        print (random.randint(1,100))

    background.join()
    print ("With background.join we wait for the other thread to complete")


if __name__ == "__main__":
    Main()