from threading import Semaphore

sem_initial_value = 3
## Semaphore object is initialised with "sem_initial_value" number of tickets
my_semaphore = Semaphore(sem_initial_value)

## "my_semaphore._value" let us access current number of tickets
print(f"value of semaphore: {my_semaphore._value}")

## acquire() method is P(), so process which invoke acquire for semaphore can be blocked
## if there is not enough tickets
my_semaphore.acquire()

## run the code, observe its behaviour
## what was printed on a console?
## does the process (thread) ended (Process finished with exit code 0) or not
## try to change semaphore initial value, run and analyse results
## you can "produce" tickets by invoking release method (V() procedure)
## my_semaphore.release()

print("hello world 1")
print(f"value of semaphore: {my_semaphore._value}")

my_semaphore.acquire()

print("hello world 2")
print(f"value of semaphore: {my_semaphore._value}")

my_semaphore.acquire()
print("hello world 3")
print(f"value of semaphore: {my_semaphore._value}")