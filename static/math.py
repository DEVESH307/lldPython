# 0. Static Method (Original Code)
# class Math:
#     @staticmethod
#     def add(self, a,b):
#         return a+b

# print(Math().add(5,7))

# 1. Static Method (Without object creation)
# class Math:
#     def add(self, a,b):
#         return a+b

# print(Math.add(5,7))
# # output: TypeError: Math.add() missing 1 required positional argument: 'b'

# # 2. Static Method (with object creation) 
# class Math:
#     def add(self, a,b):
#         return a+b

# print(Math().add(5,7))
# # output: 12

# # 3. Static Method (Without object creation, with multiple arguments) 
# class Math:
#     # x itself is self
#     def add(x,a,b):
#         c = x.subtract(a, b)
#         return c
#     def subtract(x,a,b):
#         return a-b

# print(Math.add(4, 5,7))
# # output: AttributeError: 'int' object has no attribute 'subtract'


# 4. Static Method (with static method decorator) 
class Math:
    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(5,7))
# output: 12
# static method is used when you want to call a method without creating an instance of the class.
# static method examle Math.round(5.6), Math.floor(5.6), Math.ceil(5.6)

import math
x = math.sqrt(64)
print(x)