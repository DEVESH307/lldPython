# # 0. Hello World with Threads(Original Code)
# import threading
# import concurrent.futures
# import time


# def hello_world(t):

#     time.sleep(t)

#     return f"Hello World! from {threading.current_thread().name}"



# time1 = time.perf_counter()


# #
# # hello_world(4)
# # hello_world(3)
# # hello_world(2)
# with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
#     f1 = executor.submit(hello_world, 4) # T1 T1 T1 T1
#     f2 = executor.submit(hello_world, 3) # T2 T2 T2
#     f3 = executor.submit(hello_world, 2) # Q  Q  Q  T2 T2

#     result3 = f3.result()
#     print(result3)

#     result1  = f1.result()
#     result2 = f2.result()

#     print(result1)
#     print(result2)



#     # print(val,val2,val3)





# # thread1 = threading.Thread(target=hello_world, args=[4], name="t-1")
# # thread2 = threading.Thread(target=hello_world,args=[3] ,name="t-2")
# # thread3 = threading.Thread(target=hello_world,args=[2] ,name="t-3")

# # thread1.start()
# # thread2.start()
# # thread3.start()
# #
# # thread1.join()
# # thread2.join()
# # thread3.join()
# time2 = time.perf_counter()

# # print..
# print(time2-time1)




# # 1. Hello World with Threads(Modified Code)
# import threading
# import concurrent.futures
# import time

# def hello_world():
#     time.sleep(0.1)
#     print(f"Hello World! from {threading.current_thread().name}")



# thread1 = threading.Thread(target=hello_world, name="t-1")
# thread2 = threading.Thread(target=hello_world, name="t-2")

# thread1.start()
# thread2.start()



# # 2. Hello World with Threads (Modified Code)
# import threading
# import concurrent.futures
# import time

# def hello_world():
#     time.sleep(0.1)
#     print(f"Hello World! from {threading.current_thread().name}")



# thread1 = threading.Thread(target=hello_world, name="t-1")
# thread2 = threading.Thread(target=hello_world, name="t-2")

# thread1.start()
# thread2.start()


# # 3. Hello World with Threads (with join)
# import threading
# import concurrent.futures
# import time

# def hello_world(t):
#     time.sleep(t)
#     print(f"Hello World! from {threading.current_thread().name}")


# # time1 = time.perf_counter()

# # hello_world(4)
# # hello_world(3)  
# # hello_world(2)

# # time2 = time.perf_counter()
# # print(time2 - time1)
# # # output: 9.002265300019644


# # time1 = time.perf_counter()

# # thread1 = threading.Thread(target=hello_world, args=[4], name="t-1")
# # thread2 = threading.Thread(target=hello_world, args=[3], name="t-2")
# # thread3 = threading.Thread(target=hello_world, args=[2], name="t-3")

# # thread1.start()
# # thread2.start()
# # thread3.start()

# # time2 = time.perf_counter()
# # print(time2 - time1)
# # # not waiting for threads to finish
# # # output: 0.001655799918808043

# time1 = time.perf_counter()
# thread1 = threading.Thread(target=hello_world, args=[4], name="t-1")
# thread2 = threading.Thread(target=hello_world, args=[3], name="t-2")
# thread3 = threading.Thread(target=hello_world, args=[2], name="t-3")

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()  
# thread3.join()

# time2 = time.perf_counter()
# print(time2 - time1)
# # output: 4.002281399909407


# # 4. Hello World with Threads (with executor)
# import threading
# import concurrent.futures # to create a thread pool (assembly line)
# import time

# def hello_world(t):
#     time.sleep(t)
#     print(f"Hello World! from {threading.current_thread().name}")


# time1 = time.perf_counter()

# # if max_workers (max no of thread) = 1 => sequential thread
# # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
# #     f1 = executor.submit(hello_world, 4)  # T1 T1 T1 T1
# #     f2 = executor.submit(hello_world, 3)  # Q  Q  Q T1 T1 T1
# #     f3 = executor.submit(hello_world, 2)  # Q  Q  Q T1 T1 

# # time2 = time.perf_counter()
# # print(time2 - time1)
# # # output: 9.006413600058295

# # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
# #     f1 = executor.submit(hello_world, 4)  # T1 T1 T1 T1
# #     f2 = executor.submit(hello_world, 3)  # T2 T2 T2
# #     f3 = executor.submit(hello_world, 2)  # Q  Q  Q  T2 T2

# # time2 = time.perf_counter()
# # print(time2 - time1)
# # # output: 5.008118800004013

# # max_workers=3 means 3 threads can run concurrently
# # max_workers=10000 means 10000 threads can run concurrently but it will not create 10000 threads, it will create only as many threads as needed to complete the tasks
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     f1 = executor.submit(hello_world, 4)  # T1 T1 T1 T1
#     f2 = executor.submit(hello_world, 3)  # T2 T2 T2
#     f3 = executor.submit(hello_world, 2)  # T3 T3

# time2 = time.perf_counter()
# print(time2 - time1)
# # output: 4.00592649995815




# # 4. Hello World with Threads (with executor and future)
# import threading
# import concurrent.futures # to create a thread pool (assembly line)
# import time

# def hello_world(t):
#     time.sleep(t)
#     return f"Hello World! from {threading.current_thread().name}"


# time1 = time.perf_counter()

# with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
#     val1 = executor.submit(hello_world, 4)  # T1 T1 T1 T1
#     val2 = executor.submit(hello_world, 3)  # T2 T2 T2
#     val3 = executor.submit(hello_world, 2)  # T3 T3
    
#     print(val1, val2, val3)

# time2 = time.perf_counter()
# print(time2 - time1)
# # output: <Future at 0x2b5ee577230 state=running> <Future at 0x2b5ee567890 state=running> <Future at 0x2b5ee567d90 state=running>
# # output: 4.004756800015457


# 4. Hello World with Threads (with executor and future and result)
import threading
import concurrent.futures # to create a thread pool (assembly line)
import time

def hello_world(t):
    time.sleep(t)
    return f"Hello World! from {threading.current_thread().name}"


time1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
    f1 = executor.submit(hello_world, 4)  # T1 T1 T1 T1
    f2 = executor.submit(hello_world, 3)  # T2 T2 T2
    f3 = executor.submit(hello_world, 2)  # T3 T3
    
    # result1 = f1.result()  # This will block until the result is available
    # result2 = f2.result()  # This will block until the result is available
    # result3 = f3.result()  # This will block until the result is available
    
    # # all results are available now and printed simultaneously
    # print(result1)
    # print(result2)
    # print(result3)
    
    result3 = f3.result()  # This will block until the result is available
    print(result3)  # This will print the result of f3 immediately after it is available
    result1 = f1.result()  # This will block until the result is available
    result2 = f2.result()  # This will block until the result is available
    
    # all results are available now and printed simultaneously
    print(result1)
    print(result2)

time2 = time.perf_counter()
print(time2 - time1)
# output: 