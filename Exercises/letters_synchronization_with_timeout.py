import random
from threading import Semaphore, Thread

sem_a = Semaphore(1)
sem_b = Semaphore(0)
sem_c = Semaphore(0)

COUNT = 5

def print_a():

    for seq_no in range(COUNT):

        if sem_a.acquire(timeout=0.5):
            print(f"\nsequence number: {seq_no} ")
            print('A ', end='')
            sem_b.release()
        else:
            print("process print_a could not acquire for sequence number: ", seq_no)


def print_b():

    for _ in range(COUNT):
        if sem_b.acquire(timeout=0.5):
            print('B ', end='')
            sem_c.release()
        else:
            print("\nprocess print_b could not acquire")


def print_c():

    for _ in range(COUNT):
        if sem_c.acquire(timeout=0.5):
            print('C ', end='')
            sem_a.release()
        else:
            print("\nprocess print_c could not acquire")


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