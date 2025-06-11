# # 0. Typing and Generics in Python(Original Code)
# from typing import List, Optional, Any

# # age: int = 10
# #
# # print(age)
# # age = 10
# #
# # print(age)


# #  Typing techniques..

# sqr: float = 0


# def squareDiveideBy2(num: float) -> float:
#     print(num * num)
#     return num * num // 2


# sqr = squareDiveideBy2(10.00)


# def square(num: float) -> None:
#     print(num * num)


# square(10.00)

# # numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers)

# numbDict: dict[int, str] = {1: "abc", 2: "def", 3: "ghi"}
# # numbDict: dict[int, str] = {1:"abc", 2:"def","ghi": 3}

# print(numbDict)

# # numbSet: set[str] = {"abc","def","ghi", 2}
# numbSet: set[str] = {"abc", "def", "ghi"}

# print(numbSet)

# # ll: list[list[int]]  = [[1,"asn",5], [2,4,5]]
# ll: list[list[int]] = [[1, 2, 5], [2, 4, 5]]

# vector = list[list[int]]

# ll2: vector = [[1, 2, 5], [2, 4, 5]]

# print(ll2)


# def greet(name: Optional[str] = None) -> str:
#     return f"Hello {name}"


# print(greet())


# def printingMethod(val: Any):
#     print(val)


# printingMethod(["1"])


# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age


# def getPersonName(person: Person) -> str:
#     return person.name


# getPersonName(Person("John", 20))

# # GENERICS..

# from typing import Generic, TypeVar, Type

# M = TypeVar('M')


# class Stack(Generic[M]):
#     def __init__(self) -> None:
#         self.stack: list[M] = []

#     def push(self, item: M) -> None:
#         self.stack.append(item)

#     def pop(self) -> M:
#         return self.stack.pop()


# stack1 = Stack[int]()

# # class StackInt():
# #     def __init__(self) -> None:
# #         self.stack: list[int] = []
# #
# #     def push(self, item: int) -> None:
# #         self.stack.append(item)
# #
# #     def pop(self) -> int:
# #         return self.stack.pop()


# T = TypeVar('T', int, float)


# def add(a1: T, a2: T) -> T:
#     return a1 + a2


# add(1.0, 1.0)


# class A:
#     def __init__(self, x: int) -> None:
#         self.x = x

# class B(A):
#     def __init__(self, x: int) -> None:
#         self.x = x
#         super().__init__(x)

# class C(A):
#     def __init__(self, x: int) -> None:
#         self.x = x
#         super().__init__(x)

# G = TypeVar('G', bound=A)


# 1. Typing and Generics in Python(Modified Code)
# pip install mypy
# mypy .\datatypeTyping.py
# mypy --strict .\datatypeTyping.py
# mypy .

from typing import List, Optional, Any

# age: int = 10
# print(age)
# # output: 10

# age = "I don't know"
# print(age)
# # output: error

# age = 20
# print(age)
# # output: 20

# age = 10.00
# print(age)
# # output: error


# def square(num):
#     return num * num

# print(square(10))
# print(square(10.00))
# # output: no error for both calls

# sqr: int = 0 # error
# sqr: float = 0 # no error
# def squareDivideBy2(num: float) -> float:
#     return num * num // 2

# sqr = squareDivideBy2(10.00)
# print(sqr)


# def square(num: float) -> None:
#     print(num * num)

# square(10.00)
# # no error

# def squaredivideBy2(num: float) -> float:
#     print(num * num)
#     return num * num // 2

# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # no error
# print(numbers)
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"] # error
# print(numbers)

# dict_numbers: dict[int, str] = {1: "abc", 2: "def", 3: "ghi"} # no error
# print(dict_numbers)
# dict_numbers: dict[int, str] = {1: "abc", 2: "def", "ghi": 3} # error
# print(dict_numbers)

# numbSet: set[str] = {"abc", "def", "ghi"}  # no error
# print(numbSet)
# numbSet: set[str] = {"abc", "def", "ghi", 2}  # error
# print(numbSet)

# ll: list[list[int]] = [[1, 2, 5], [2, 4, 5]]  # no error
# ll: list[list[int]] = [[1, "abc", 5], [2, 4, 5]]  # no error

# if list of lists is used multiple times, we can use type aliasing
# vector = list[list[int]]
# ll2: vector = [[1, 2, 5], [2, 4, 5]]  # no error

# def greet(name: str = None) -> str:
#     return f"Hello {name}"

# print(greet()) # error
# print(greet("Devesh")) # error


# def greet(name: Optional[str] = None) -> str:
#     return f"Hello {name}"

# print(greet()) # no error
# print(greet("Devesh")) # no error


# def printingMethod(val: Any)->None:
#     print(val)

# printingMethod(["1"])  # no error
# printingMethod(1)  # no error
# printingMethod(1.0)  # no error
# printingMethod({"key": "value"})  # no error

# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

# def getPersonName(person: Person) -> str:
#     return person.name

# getPersonName(Person("John", 20))  # no error
# getPersonName("John")  # error
# getPersonName(20)  # error


# GENERICS..
from typing import Generic, TypeVar

# # stack using str
# class stack():
#     def __init__(self) -> None:
#         self.stack: list[str] = []

#     def push(self, item: str) -> None:
#         self.stack.append(item)

#     def pop(self) -> str:
#         return self.stack.pop()    

# # stack using int
# class stack():
#     def __init__(self) -> None:
#         self.stack: list[int] = []

#     def push(self, item: int) -> None:
#         self.stack.append(item)

#     def pop(self) -> int:
#         return self.stack.pop()


# # stack using Generics placeholder(any type)
# # T = TypeVar('T')  # Type variable that can be any type
# placeholder = TypeVar('placeholder')
# class stack(Generic[placeholder]):
#     def __init__(self) -> None:
#         self.stack: list[placeholder] = []

#     def push(self, item: placeholder) -> None:
#         self.stack.append(item)

#     def pop(self) -> placeholder:
#         return self.stack.pop()
    
# stack1 = stack[int]() # can take only int values
# # stack1 = stack[Any]() # can tak mix types values


# T = TypeVar('T', int, float)

# def add(a1: T, a2: T) -> T:
#     return a1 + a2

# add(1, 2)  # no error
# add(1.0, 2.0)  # no error
# add(1, 2.0)  # no error
# add("1", "2")  # error
# add(1, "2")  # error


class A:
    def __init__(self, x: int) -> None:
        self.x = x

class B(A):
    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)

class C(A):
    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)

G = TypeVar('G', bound=A)
def process_instance(instance: G) -> None:
    print(f"Processing instance of {instance.__class__.__name__} with x = {instance.x}")

process_instance(A(10))  # no error
process_instance(B(20))  # no error
process_instance(C(30))  # no error