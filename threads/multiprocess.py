# # 0. Hello World with Multiprocessing (Original Code)
# import multiprocessing
# import time

# def hello_world(t):

#     time.sleep(t)

#     print(f"Hello World! from {multiprocessing.current_process().name}")


# time1 = time.perf_counter()


# #
# # hello_world(4)
# # hello_world(3)
# # hello_world(2)
# #

# if __name__ == '__main__':
#     process1 = multiprocessing.Process(target=hello_world, args=(4,))
# #

#     process1.start()
# # thread2.start()
# # thread3.start()

#     process1.join()
# # thread2.join()
# # thread3.join()
#     time2 = time.perf_counter()

# # print..
#     print(time2-time1)




# 1. Hello World with Multiprocessing (Modified Code)
import multiprocessing
import time

def hello_world(t):
    time.sleep(t)
    print(f"Hello World! from {multiprocessing.current_process().name}")


if __name__ == '__main__':
    # Ensure the code runs only when the script is executed directly and not when imported as a module.
    time1 = time.perf_counter()

    process1 = multiprocessing.Process(target=hello_world, args=(4,))
    # process2 = multiprocessing.process(target=hello_world, args=(3,))
    # process3 = multiprocessing.process(target=hello_world, args=(2,))

    process1.start()
    # process2.start()
    # process3.start()

    process1.join()
    # process2.join()  
    # process3.join()

    time2 = time.perf_counter()
    print(time2 - time1)

# output:
# Hello World! from Process-1
# 4.190865799901076