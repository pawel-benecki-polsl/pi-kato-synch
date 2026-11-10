from threading import Semaphore
#from threading import Lock
from threading import Thread
#import threading
from time import sleep
#import time
import random

BUFFER_SIZE = 5
buffer = []

empty = Semaphore(BUFFER_SIZE)
full = Semaphore(0)
#mutex = Lock()
access = Semaphore(1)


def producer():
    while True:
        item = random.randint(1,10)
        empty.acquire()
        #mutex.acquire()
        access.acquire()
        buffer.append(item)
        print(f"produced {item}, buffer {buffer}")
        #mutex.release()
        access.release()
        full.release()
        #sleep(random.uniform(0.5,2)) #production time
        sleep(1)

def consumer():

    while True:

        full.acquire()
        #mutex.acquire()
        access.acquire()

        item = buffer.pop(0)
        print(f"consumed {item}, buffer {buffer}")
        #mutex.release()
        access.release()
        empty.release()
        #sleep(random.uniform(0.5,2)) #consumption time
        sleep(2)

print(f"full: {full._value}")
print(f"empty: {empty._value}")
producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

#below never happens because of while true
producer_thread.join()
consumer_thread.join()