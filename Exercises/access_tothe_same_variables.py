
from threading import Semaphore, Thread

#sem_A = Semaphore(1)

X = 10
Y = 5

def print_variables():
    global X, Y
    print(f"X = {X}, Y = {Y}")
    #reset values
    X = 10
    Y = 5

def first_thread():
    global X

    X = X + Y


def second_thread():
    global Y

    Y = Y + X

threads = [Thread(target=first_thread), Thread(target=second_thread)]

for thread in threads:
    thread.start()
#wait for threads to end
for thread in threads:
    thread.join()

print_variables()

#start threads in different order
threads = [Thread(target=second_thread), Thread(target=first_thread)]

for thread in threads:
    thread.start()
#wait for threads to end
for thread in threads:
    thread.join()

print_variables()

print("All done")