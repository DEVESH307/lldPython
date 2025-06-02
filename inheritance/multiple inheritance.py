# # 0. Multiple Inheritance Example (Original Code)
# class Base:
#     def __init__(self):
#         print("Base class constructor")
#         self.base_attr = "Base attribute"

#     def base_method(self):
#         print("Base method")

# class parent1(Base):
#     def __init__(self):
#         print("parent 1 const..")
#         self.nose = 1
#     def func(self):
#         print("parent 1..")

#     def func1(self):
#         print("func 1..")

# class parent2(Base):
#     def __init__(self):
#         print("parent 2 const..")
#         self.name = "abc"

#     def func(self):
#         print("parent 2..")


# class child(parent1, parent2):
#     def __init__(self):
#         # parent1.__init__(self)
#         parent2.__init__(self)


# c = child()
# # output: parent 2 const..
# print(c.func())
# # output: parent 1..
# # output: None
# parent2.func(c)
# # output: parent 2..
# print(c.func1())
# # output: func 1..
# # output: None
# # print(child.mro())
# # output: [<class '__main__.child'>, <class '__main__.parent1'>, <class '__main__.parent2'>, <class '__main__.Base'>, <class 'object'>]
# # print(dir(c))
# # output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'base_attr', 'base_method', 'func1', 'name', 'nose']


# # 1. Multiple Inheritance Example with Constructor and Method Overriding
# class parent1():
#     def __init__(self):
#         print("parent 1 const..")
#         self.nose = 1

#     def func(self):
#         print("parent 1..")

# class parent2():
#     def __init__(self):
#         print("parent 2 const..")
#         self.name = "abc"
        
#     def func(self):
#         print("parent 2..")


# class child(parent1, parent2):
#     def __init__(self):
#         super().__init__()
#         pass

# c = child()
# # output: parent 1 const..
# parent1.func(c)
# # output: parent 1..
# print(c.nose)
# # output: 1
# # print(c.name)
# # output: AttributeError: 'child' object has no attribute 'name'


# # 2. Multiple Inheritance with Constructor and Method Overriding with MRO
# class parent1():
#     def __init__(self):
#         print("parent 1 const..")
#         self.nose = 1
        
#     def func(self):
#         print("parent 1..")

# class parent2():
#     def __init__(self):
#         print("parent 2 const..")
#         self.name = "abc"
        
#     def func(self):
#         print("parent 2..")


# class child(parent1, parent2):
#     def __init__(self):
#         # parent2.__init__(self)
#         parent1.__init__(self)
#         parent2.__init__(self)


# c = child()
# # output: parent 1 const..
# parent1.func(c)
# # output: parent 1..
# print(c.nose)
# # output: 1
# print(c.name)
# # output: ab


# 2. Multiple Inheritance with Constructor and Method Overriding (with MRO)
class parent1():
    def __init__(self):
        print("parent 1 const..")
        self.nose = 1
        
    def func1(self):
        print("parent 1..")

class parent2():
    def __init__(self):
        print("parent 2 const..")
        self.name = "abc"
        
    def func(self):
        print("parent 2..")


class child(parent1, parent2):
    def __init__(self):
        # parent1.__init__(self)
        parent2.__init__(self)


c = child()
# output: parent 2 const..
parent1.func1(c)
# output: parent 1..
print(c.func1())
# output: parent 1..
# output: None
# print(c.nose)
# output: AttributeError: 'child' object has no attribute 'nose'
print(c.name)
# output: ab



