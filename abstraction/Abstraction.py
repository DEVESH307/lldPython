# # 0. Abstraction (Original Code)
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, num_of_tires):
#         self.num_of_tires = num_of_tires

#     @abstractmethod
#     def start(self):
#         pass

# # v = Vehicle(1) # error..
# #
# # print(v.num_of_tires)

# class car(Vehicle):
#     def __init__(self, num_of_tires, color):
#         super().__init__(num_of_tires)
#         self.color = color

#     def start(self):
#         print("asnc")

# c = car(4, "red")
# c.start()
# print(c.color)

# class bike(Vehicle):
#     def __init__(self, num_of_tires, color):
#         super().__init__(num_of_tires)
#         self.color = color

#     def start(self):
#         print("bike started with kick..")

# b = bike(2, "blue")
# b.start()

# class cycle(Vehicle):
#     def __init__(self, num_of_tires, color):
#         pass

#     def start(self):
#         print("started cycle..")

# def startVehicle(v):
#     # 1000 things... v.unlock()
#     v.start()

# #     1000 things..

# startVehicle(b)
# startVehicle(c)
# cycles = cycle(1,"red")
# startVehicle(cycles)


# #

# # def greet(hello):
# #     def mfx(*args, **kwargs):
# #         print("hi karan..")
# #         hello(*args, **kwargs)
# #         print("thanks karan..")
# #
# #     return mfx
# #
# #
# # @greet
# # def hello():
# #     print("Hello")
# #
# # hello()



# # 1. Abstraction (Using Abstract Base Class, can't instantiate abstract class Vehicle)
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self, num_of_tires):
#         self.num_of_tires = num_of_tires

#     @abstractmethod
#     def start(self):
#         pass
#         # raise NotImplementedError("Subclasses must implement this method.")
    
# v = Vehicle(1)
# print(v.num_of_tires)
# # output: TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract method 'start'


# # 1.1 Abstraction (Using method overloading won't work, take last method as implementation)
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self, num_of_tires):
#         self.num_of_tires = num_of_tires

#     @abstractmethod
#     def start(self):
#         pass
#         # raise NotImplementedError("Subclasses must implement this method.")
#     def start(self, ignition=None):
#         if ignition:
#             print("Vehicle started with ignition..")
#         else:
#             print("Vehicle started without ignition..")

# v = Vehicle(1)
# print(v.num_of_tires) # output: 1
# v.start()  # output: Vehicle started without ignition..
# v.start(2)  # output: Vehicle started with ignition..


# # 2. Abstraction (abstract method not implemented error)
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self, num_of_tires):
#         self.num_of_tires = num_of_tires

#     @abstractmethod
#     def start(self):
#         pass
#         # raise NotImplementedError("Subclasses must implement this method.")
        
# class Car(Vehicle):
#     def __init__(self, num_of_tires, color):
#         super().__init__(num_of_tires)
#         self.color = color

#     # def start(self):
#     #     print("Car started with ingnition..") 

# c = Car(4, "red")
# print(c.num_of_tires)  # Output: error: Can't instantiate abstract class Car without abstract method start
# print(c.color)        # Output: error: Can't instantiate abstract class Car without abstract method start


# 3. Abstraction (Using Decorators)
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, num_of_tires):
        self.num_of_tires = num_of_tires

    @abstractmethod
    def start(self):
        pass
        # raise NotImplementedError("Subclasses must implement this method.")
        
class Car(Vehicle):
    def __init__(self, num_of_tires, color):
        super().__init__(num_of_tires)
        self.color = color

    def start(self):
        print("Car started with ingnition..")

class Bike(Vehicle):
    def __init__(self, num_of_tires, color):
        super().__init__(num_of_tires)
        self.color = color

    def start(self):
        print("Bike started with kick..")

class Cycle(Vehicle):
    def __init__(self, num_of_tires, color):
        super().__init__(num_of_tires)
        self.color = color

    def start(self):
        print("Cycle started with pedaling..")

# # class A is not a abastract class, so it cannot be used as a Vehicle
# class A():
#     def __init__(self, num_of_tires, color):
#         pass

def startVehicle(v: Vehicle):
    # Ensure the vehicle is unlocked before starting
    # 1000 things... v.unlock()
    v.start()

# a = A(4, "red")
# startVehicle(a)  # Output: TypeError: startVehicle() argument must be Vehicle instance, not A

c = Car(4, "red")
print(c.num_of_tires)  # Output: 4
print(c.color)        # Output: red
c.start()  # Output: Car started with ingnition..
startVehicle(c)  # Output: Car started with ingnition..

b = Bike(2, "blue")
print(b.num_of_tires)  # Output: 2  
print(b.color)        # Output: blue
b.start()  # Output: Bike started with kick..
startVehicle(b)  # Output: Bike started with kick..

cycles = Cycle(2, "black")
print(cycles.num_of_tires)  # Output: 2
print(cycles.color)        # Output: black 
cycles.start()  # Output: Cycle started with pedaling..
startVehicle(cycles)  # Output: Cycle started with pedaling..


# --------------------------------Decorator--------------------------------
# # Decorator to greet before and after the function call (used in login)
# def greet(func):
#     def wrapper(*args, **kwargs):
#         print("Hi Devesh")
#         func(*args, **kwargs)
#         print("Thanks Devesh")
#     return wrapper

# @greet
# def hello():
#     print("Hello")

# hello()
# # greet(hello)() # hello() is already wrapped but greet(hello) again → double wrapped

# # Without Decorator
# def greet(func):
#     def wrapper(*args, **kwargs):
#         print("Hi Devesh")
#         func(*args, **kwargs)
#         print("Thanks Devesh")
#     return wrapper

# def hello():
#     print("Hello")

# greet(hello)()
