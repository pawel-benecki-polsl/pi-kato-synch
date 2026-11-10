from time import sleep
from threading import Semaphore, Thread
import random
# run this code few times, compare results

COUNT = 10
SLEEP_TIME = 0.1

def print_a():
    for _ in range(COUNT):
        print('A ', end='')
        sleep(SLEEP_TIME)

def print_b():
    for _ in range(COUNT):
        print('B ', end='')
        sleep(SLEEP_TIME)

def print_c():
    for _ in range(COUNT):
        print('C ', end='')
        sleep(SLEEP_TIME)


threads = [] #list of threads
threads.append(Thread(target=print_a, name="printA"))
threads.append(Thread(target=print_b, name="printB"))
threads.append(Thread(target=print_c, name="printC"))
# to start threads in random order
random.shuffle(threads)
#print start order
for thread in threads:
    print(thread.name)
#start threads
for thread in threads:
    thread.start()
#wait for threads to end
for thread in threads:
    thread.join()
print("\nAll done")