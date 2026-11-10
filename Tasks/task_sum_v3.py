import random
from threading import Semaphore, Thread

A = 1
B = 2
C = 3

def process_p1():
    global A, B, C

    A = A + C
    B = B + 4
    C = C + A


def process_p2():
    global A, B, C

    B = B + C
    A = A + B
    C = B + 5


def process_p3():
    global A, B, C

    A = 2 * B
    B = B + A


def print_sum():
    global A, B, C

    print(f'{A} + {B} + {C} = {A + B + C}')

threads = []
threads.append(Thread(target=process_p1, name="P1"))
threads.append(Thread(target=process_p2, name="P2"))
threads.append(Thread(target=process_p3, name="P3"))
threads.append(Thread(target=print_sum, name="print_sum"))
# shuffle to start threads in random order
random.shuffle(threads)
# print start order
for thread in threads:
    print(thread.name)
# start threads
for thread in threads:
    thread.start()
# wait for threads to end
for thread in threads:
    thread.join()
print("\nAll done")