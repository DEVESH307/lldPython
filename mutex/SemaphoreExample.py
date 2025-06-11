# # 0. semaphore Example(original code)
# from threading import *

# import time

# obj = Semaphore(0)
# def display(name):
#     obj.acquire()
#     for i in range(1):
#         print("Hello "+name)
#         time.sleep(0.5)
#     obj.release()


# t1 = Thread(target=display, args=("t1",))
# t2 = Thread(target=display, args=("t2",))
# t3 = Thread(target=display, args=("t3",))
# t4 = Thread(target=display, args=("t4",))
# t5 = Thread(target=display, args=("t5",))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()


# # 1. semaphore Example with deadlock (Modified Code)
# from threading import *
# import time

# # obj = Semaphore() # Default value is 1, meaning one thread can access the resource at a time
# obj = Semaphore(4) # Allow up to 4 threads to access the resource concurrently
# def display(name):
#     obj.acquire()
#     obj.acquire()
#     obj.acquire()
#     obj.acquire()
#     obj.acquire()
#     for i in range(5):
#         print("Hello " + name)
#         time.sleep(0.5)
#     obj.release()

# t1 = Thread(target=display, args=("t1",))
# t2 = Thread(target=display, args=("t2",))
# t3 = Thread(target=display, args=("t3",))
# t4 = Thread(target=display, args=("t4",))
# t5 = Thread(target=display, args=("t5",))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# # Wait for all threads to complete
# # output: Deadlocak occurs because each thread tries to acquire the semaphore 5 times, but only 4 threads can run concurrently.


# # 2. semaphore Example (modified Code)
# from threading import *
# import time

# obj = Semaphore(4) # 4 2 3 1 2 0
# def display(name):
#     obj.acquire()
#     obj.acquire()
#     for i in range(5):
#         print("Hello " + name)
#         time.sleep(0.5)
#     obj.release()

# t1 = Thread(target=display, args=("t1",))
# t2 = Thread(target=display, args=("t2",))
# t3 = Thread(target=display, args=("t3",))
# t4 = Thread(target=display, args=("t4",))
# t5 = Thread(target=display, args=("t5",))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# # Wait for all threads to complete
# # output: deadloack occurs acquire 2 times, but release only once, so it will not release the semaphore for other threads to acquire.


# # 3. semaphore Example with Threads (Modified Code)
# from threading import *
# import time

# obj = Semaphore(4) 
# def display(name):
#     obj.acquire()
#     for i in range(5):
#         print("Hello " + name)
#         time.sleep(0.5)
#     obj.release()

# t1 = Thread(target=display, args=("t1",))
# t2 = Thread(target=display, args=("t2",))
# t3 = Thread(target=display, args=("t3",))
# t4 = Thread(target=display, args=("t4",))
# t5 = Thread(target=display, args=("t5",))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# # Wait for all threads to complete
# # output: Hello t1
# # Hello t2 ..............


# 4. semaphore Example with producer-consumer (Modified Code)
from threading import Thread, Semaphore, Lock
import time
import random

buffer = []
buffer_size = 5

# Semaphores
empty_slots = Semaphore(buffer_size)  # Initially all slots are empty
filled_slots = Semaphore(0)           # No filled slots initially

# Lock for thread-safe buffer access
buffer_lock = Lock()

def producer():
    for i in range(10):
        item = random.randint(1, 100)
        empty_slots.acquire()  # Wait if buffer is full
        with buffer_lock:
            buffer.append(item)
            print(f"Producer produced: {item}")
        filled_slots.release()  # Signal consumer
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    for i in range(10):
        filled_slots.acquire()  # Wait if buffer is empty
        with buffer_lock:
            item = buffer.pop(0)
            print(f"Consumer consumed: {item}")
        empty_slots.release()  # Signal producer
        time.sleep(random.uniform(0.2, 0.6))

# Create and start threads
producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
# output: Producer produced: 27
# Consumer consumed: 27
# Producer produced: 45............