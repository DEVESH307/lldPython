# # 0. Define an interface for workers that can work and eat(original code)
# from abc import ABC, abstractmethod
# class Worker(ABC):
#     @abstractmethod
#     def work(self):
#         pass

# class EatableWorker(ABC):

#     @abstractmethod
#     def eat(self):
#         pass

# class Human(Worker, EatableWorker):
#     def eat(self):
#         print('eat')

#     def work(self):
#         print('work')

# class Robot(Worker):
#     def work(self):
#         print('work')


# 1. Define an interface for switchable devices(refactored code)
from abc import ABC, abstractmethod
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    def eat(self):
        pass

class EatableWorker(Worker):
    @abstractmethod
    def eat(self):
        pass
    
class Human(Worker, EatableWorker):
    def eat(self):
        print('Human eating')

    def work(self):
        print('Human working')

class Robot(Worker):
    def work(self):
        print('Robot working')