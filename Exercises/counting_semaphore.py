from threading import Semaphore

sem_initial_value = 3
my_semaphore = Semaphore(sem_initial_value)

no_of_iterations = 5
i = 0
print(f"initial value of semaphore: {my_semaphore._value}")

for _ in range (no_of_iterations):
    ## acquire method with timeout parameter in seconds,
    ## if there is no ticket for semaphore, thread will wait for "timeout" seconds
    ## if no ticket will be available thread will continue its work
    ## WITHOUT ACCESSING RESOURCE - IN OUR CASE RESOURCE IS i VARIABLE
    ## run the code, analyse results, change sem_initial_value/no_of_iterations, observe results
    if my_semaphore.acquire(timeout=1):
        i = i + 1
    print(f"i value: {i}")
    print(f"value of semaphore: {my_semaphore._value} \n")

print(f"end i value {i}")