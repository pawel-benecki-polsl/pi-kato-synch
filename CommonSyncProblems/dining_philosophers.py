from threading import Semaphore
#from threading import Lock
from threading import Thread
#import threading
from time import sleep
#import time
import random

PHILO_NUMBER = 5

#fork for each philosopher
forks = [Semaphore(1) for _ in range(PHILO_NUMBER)]

def philosopher(id):
    while True:
        # thinking
        print(f"Philosopher {id} is thinking...")
        sleep(random.uniform(0.5, 2))

        # picking forks
        left_fork = id
        right_fork = (id+1) % PHILO_NUMBER

        # pick up lower numbered fork first
        first_fork = min(left_fork, right_fork)
        second_fork = max(left_fork, right_fork)

        # acquiring forks
        print(f"Philosopher {id} is trying to pick up forks...")
        forks[first_fork].acquire()
        print(f"Philosopher {id} picked up 1 fork {first_fork}...")
        forks[second_fork].acquire()
        print(f"Philosopher {id} picked up 2 fork {second_fork}...")

        # eating
        print(f"Philosopher {id} is eating...")
        sleep(random.uniform(1, 3))

        # putting down forks
        forks[first_fork].release()
        print(f"Philosopher {id} put down 1 fork {first_fork}...")
        forks[second_fork].release()
        print(f"Philosopher {id} put down 2 fork {second_fork}...")


for i in range(PHILO_NUMBER):
    Thread(target=philosopher, args=(i,)).start()