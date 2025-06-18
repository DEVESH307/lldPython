# # 0. Singleton Design Pattern(Original Code)
# import threading

# class singleton:
#     ___instance = None
#     __lock = threading.Lock()

#     def __new__(cls, *args, **kwargs):
#         if cls.___instance is None:
#             with cls.__lock:
#                 if cls.___instance is None:
#                     cls.___instance = super().__new__(cls)
#         return cls.___instance


# if __name__ == "__main__":
#     instance = singleton()
#     print(instance)
#     instance2 = singleton()
#     print(instance2)
#     print(instance is instance2)

# # TODO: H.W
# # Create Logger: implement singleton DP in that..
# #  and TEST Above code in multithreaded env..


# # 1. Singleton Design Pattern (Simplified Version without Locking)
# class Singleton:
#     ___instance = None
#     # __lock = threading.Lock()
#
#     def __new__(cls, *args, **kwargs):
#         if cls.___instance is None:
#             cls.___instance = super().__new__(cls)
#             # cls.___instance = Singleton().___instance # RecursionError: maximum recursion depth exceeded
#         return cls.___instance
#
# if __name__ == "__main__":
#     instance = Singleton()
#     print(instance)
#     instance2 = Singleton()
#     print(instance2)
#     print(instance is instance2)  # True, both are the same instance


# # 2. Singleton Design Pattern (Using a Thread-Safe Decorator)
# import threading
#
# class Singleton:
#     ___instance = None
#     __lock = threading.Lock()
#
#     def __new__(cls, *args, **kwargs):
#         if cls.___instance is None:
#             with cls.__lock:
#                 if cls.___instance is None:
#                     cls.___instance = super().__new__(cls)
#         return cls.___instance
#
# if __name__ == "__main__":
#     instance = Singleton()
#     print(instance)
#     instance2 = Singleton()
#     print(instance2)
#     print(instance is instance2)  # True, both are the same instance
#

# # TODO: H.W
# # Create Logger: implement singleton DP in that..
# #  and TEST Above code in multithreaded env..

# # 2. Singleton Logger Implementation (Thread-Safe)
# import threading
#
# class Logger:
#     ___instance = None
#     __lock = threading.Lock()
#
#     def __new__(cls, *args, **kwargs):
#         if cls.___instance is None:
#             with cls.__lock:
#                 if cls.___instance is None:
#                     cls.___instance = super().__new__(cls)
#         return cls.___instance
#     @staticmethod
#     def log(message):
#         print(f"[LOG]: {message}")
#
# def create_logger__instance():
#     logger = Logger()
#     print(f"Logger instance id: {id(logger)}")
#
# if __name__ == "__main__":
#     threads = []
#     for i in range(5):
#         t = threading.Thread(target=create_logger__instance)
#         threads.append(t)
#         t.start()
#
#     for t in threads:
#         t.join()


# 3. Thread-Safe Singleton Logger Implementation
import threading

# Singleton Logger Class
class Logger:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    print("[Logger] Creating new instance...")
                    cls.__instance = super(Logger, cls).__new__(cls)
                    cls.__instance._id = id(cls.__instance)
        return cls.__instance

    def log(self, message):
        print(f"[Logger ID: {self._id}] {message}")

# Test function to be run by multiple threads
def thread_test(thread_num):
    logger = Logger()
    logger.log(f"Message from thread {thread_num}")

# Main block for testing
if __name__ == "__main__":
    print("[Main] Starting thread-safe singleton test...\n")

    threads = []
    for i in range(5):
        t = threading.Thread(target=thread_test, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[Main] Verifying singleton instance identity...")
    logger1 = Logger()
    logger2 = Logger()
    print(f"Logger1 ID: {id(logger1)}")
    print(f"Logger2 ID: {id(logger2)}")
    print("Same instance:", logger1 is logger2)
