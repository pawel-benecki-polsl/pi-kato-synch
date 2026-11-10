
from threading import Semaphore, Thread
from time import sleep

semA = Semaphore()
semB = Semaphore()

def first_thread():

    semA.acquire()
    sleep(1)
    print("\nFirst thread is using resource A")
    print("\n\tFirst thread is trying to access resource B")
    semB.acquire()

    print("\nFirst thread is using resource B")
    semB.release()
    semA.release()


def second_thread():

    semB.acquire()
    sleep(1)
    print("\nSecond thread is using resource B")
    print("\n\tSecond thread is trying to access resource A")
    semA.acquire()

    print("\nSecond thread is using resource A")
    semA.release()
    semB.release()

threads = [Thread(target=first_thread), Thread(target=second_thread)]

for thread in threads:
    thread.start()
#wait for threads to end
for thread in threads:
    thread.join(timeout=5)
    #thread.join()

print(f"\nvalue of semaphore A: {semA._value} \n")
print(f"value of semaphore B: {semB._value} \n")
print("All done")