# 0. Hierarchical Inheritance Example (Original Code)
class parent:
    def __init__(self):
        pass

    def func(self):
        print("parent 1..")

class child1(parent):
    def __init__(self):
        pass

    
    def func_Child(self):
        print("child 1..")

class child2(parent):
    def __init__(self):
        pass


c = child1()
c.func_Child()
# Output: child 1..
c2 = child2()
c2.func_Child() 
# output: AttributeError: 'child2' object has no attribute 'func_Child' 