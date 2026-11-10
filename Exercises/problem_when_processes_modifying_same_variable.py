from threading import Semaphore, Thread

#sem_inc = Semaphore(1)

X = 0
no_of_iterations = 100

def print_variable():

    print(f"X = {X}")


def incrementation_thread():
    global X
    for _ in range(no_of_iterations):
        X = X + 1

# we will invoke two separate threads that will run the same code defined in incremetation_thread()
# so both threads will be incrementing the global variable X in "no_of_iterations" loop iterations
# your task is to run the code, check if value of X is correct
# run few experiments with no_of_iterations equal to 1000, 10000, 100000, 1000000
# does the final X value is correct each time?
# if not, why?
# try to use semaphores to solve the problem...

threads = []
threads.append(Thread(target=incrementation_thread))
threads.append(Thread(target=incrementation_thread))


for thread in threads:
    thread.start()
#wait for threads to end
for thread in threads:
    thread.join()
# print value of X
print_variable()

print("All done")