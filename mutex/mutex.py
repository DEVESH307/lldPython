# # 0. Mutex Example with Threads(Original Code)
# import threading

# shared_variable = 0

# mutex = threading.Lock()

# def addr():
#     global shared_variable
#     for _ in range(10000000):
#         # mutex.acquire()
#         shared_variable += 1
#         # mutex.release()

# def subtr():
#     global shared_variable
#     for _ in range(10000000):
#         # mutex.acquire()
#         shared_variable -= 1
#         # mutex.release()


# thread1 = threading.Thread(target=addr)
# thread2 = threading.Thread(target=subtr)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(shared_variable)


# # 1. Normal Example
# shared_variable = 0

# def adder():
#     global shared_variable
#     for _ in range(10000):
#         shared_variable += 1
            
# def subtractor():
#     global shared_variable
#     for _ in range(10000):
#         shared_variable -= 1
        
# adder()
# subtractor()
# print(shared_variable)


# # 2. Threads Example (race condition)
# # in cPython the result almost alwasy zero
# import threading
# import time

# shared_variable = 0

# def adder():
#     global shared_variable
#     for _ in range(100000000):
#         shared_variable += 1
            
# def subtractor():
#     global shared_variable
#     for _ in range(100000000):
#         shared_variable -= 1
        
# thread1 = threading.Thread(target=adder)
# thread2 = threading.Thread(target=subtractor)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(shared_variable)
# # output: 0 or some other number


# # 2.1. Threads Example with Artificial 
# import threading
# import ctypes
# import random
# import time

# # Create a C-style shared int in memory
# shared_variable = ctypes.c_long(0)

# def adder():
#     for _ in range(1000000):
#         val = shared_variable.value
#         time.sleep(0)
#         shared_variable.value = val + 1

# def subtractor():
#     for _ in range(1000000):
#         val = shared_variable.value
#         time.sleep(0)
#         shared_variable.value = val - 1

# thread1 = threading.Thread(target=adder)
# thread2 = threading.Thread(target=subtractor)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Final value:", shared_variable.value)
# # output: 0 or some other number

# 3. Mutex Example with Threads (Modified Code) 
import threading
import time

shared_variable = 0

mutex = threading.Lock()

def adder():
    global shared_variable
    # mutex.acquire()
    for _ in range(100000000):
        mutex.acquire()
        shared_variable += 1
        mutex.release()
    # mutex.release()    

def subtractor():
    global shared_variable
    for _ in range(100000000):
        mutex.acquire()
        shared_variable -= 1
        mutex.release()
    
thread1 = threading.Thread(target=adder)
thread2 = threading.Thread(target=subtractor)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(shared_variable)
# output: 0