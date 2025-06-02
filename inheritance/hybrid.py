# 0. Hybrid Inheritance Example (Original Code)
class Parent:
    # def __init__(self, a):
    #     self.eye=3
    def __init__(self):
        self.eye = 2

    def display(self):
        # print(self.eye)
        print("display parent..")

class child(Parent):
    def __init__(self, age):
        self.eye = 1
        self.age=age

    def dummy(self):
        print("child method..")

class grand_child1(child):
    pass

class grand_child2(child):
    pass


# gc_1 = grand_child1()
# output: TypeError: child.__init__() missing 1 required positional argument: 'age'
gc_1 = grand_child1(10)
gc_1.display()
# output: display parent..
parent1 = Parent()
parent1.display()
# output: display parent..
# parent1.dummy()
# output: AttributeError: 'Parent' object has no attribute 'dummy'