import random
from threading import Semaphore, Thread

sem_a = Semaphore(0)
sem_b = Semaphore(0)
sem_c = Semaphore(0)

COUNT = 5

def print_a():

    for seq_no in range(COUNT):

        print(f"\nsequence number: {seq_no} ")
        print('A ', end='')
        sem_b.release()
        sem_b.release()
        sem_a.acquire()
        sem_a.acquire()
        sem_c.release()
        sem_c.release()
        sem_c.release()
        sem_a.acquire()
        sem_a.acquire()
        sem_a.acquire()

def print_b():

    for _ in range(COUNT*2):
        sem_b.acquire()
        print('B ', end='')
        sem_a.release()


def print_c():

    for _ in range(COUNT*3):
        sem_c.acquire()
        print('C ', end='')
        sem_a.release()


threads = []
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