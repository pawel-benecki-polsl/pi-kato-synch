import random
from threading import Semaphore, Thread

A = 1
B = 2
C = 3

semaphore1 = Semaphore(0)
semaphore2 = Semaphore(0)
semaphore_print = Semaphore(0)
semaphore_end = Semaphore(0)

def process_p1():
    global A, B, C

    semaphore1.acquire()
    A = A + C
    print(f'A = A + C')
    semaphore2.release()
    semaphore_end.acquire()
    B = B + 5
    C = C + A


def process_p2():
    global A, B, C

    B = B + C
    print(f'B = B + C')
    semaphore1.release()
    semaphore_end.acquire()
    A = A + B
    C = B + 10


def process_p3():
    global A, B, C

    semaphore2.acquire()
    A = 2 * B
    print(f'A = 2 * B')
    semaphore_print.release()
    semaphore_end.acquire()
    B = B + A


def print_sum():
    global A, B, C

    semaphore_print.acquire()
    print(f'{A} + {B} + {C} = {A + B + C}')
    semaphore_end.release(3)

threads = []
threads.append(Thread(target=process_p1, name="P1"))
threads.append(Thread(target=process_p2, name="P2"))
threads.append(Thread(target=process_p3, name="P3"))
threads.append(Thread(target=print_sum, name="print_sum"))
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