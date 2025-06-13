# # 0. Iterator and generator (original code)

# my_list = ["today", "7days..", "week"]

# data = []
# for i in my_list:
#     data.append(i)

# # return data

# iterator = iter(my_list)

# print(next(iterator)) # 1
# # complex operation and it takes 5 sec...
# # return today
# print(next(iterator))
# # return 7 days graph

# print(next(iterator))
# # return month graph...

# class my_iterator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start <= self.end:
#             temp = self.start
#             self.start+=1
#             return temp
#         else:
#             raise StopIteration

#     def __reset__(self):
#         self.start = 1

# ite = my_iterator(1, 5)

# print(next(ite))

# ite.__reset__()

# for i in ite:
#     print(i)


# #  GENERATORS...

# def my_generator():
#         yield




# #
# # gen = my_generator()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# print("fib.....")
# def fib_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# gen = fib_generator()

# for _ in range(10):
#     print(next(gen))

# for _ in range(10):
#     print(next(gen))
    
    
    
# # 1. Iterator(lazy loader) and generator (modified code)
# my_list = [1,2,3,4,5,6]
# for i in my_list:
#     print(i)

# # complex operation and it takes 5 sec...
# iterator = iter(my_list)
# print(iterator) # object
# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4
# print(next(iterator)) # 5
# print(next(iterator)) # 6
# # print(next(iterator)) # StopIteration

# # dashboard: lazy loading
# my_list = ["today graph", "week graph", "month graph"]
# for i in my_list:
#     print(i)

# iterator = iter(my_list)
# print(iterator) # object
# print(next(iterator)) # today graph
# print(next(iterator)) # week graph
# print(next(iterator)) # month graph
# # print(next(iterator)) # StopIteration

# class my_iterator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start <= self.end:
#             temp = self.start
#             self.start+=1
#             return temp
#         else:
#             raise StopIteration

#     def __reset__(self):
#         self.start = 1

# iterator = my_iterator(1, 6)

# # for i in iterator:
# #     print(i)

# print(iterator) # object
# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4
# print(next(iterator)) # 5
# print(next(iterator)) # 6
# # print(next(iterator)) # StopIteration

# # reset to zero (start)
# iterator.__reset__()
# print(iterator) # object
# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4
# print(next(iterator)) # 5
# print(next(iterator)) # 6
# # print(next(iterator)) # StopIteration


# Generators: 
# S(O) = 1
def my_generator():
    for i in range(50000000):
        yield i
        
gen = my_generator()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3

for i in range(50000000):
    print(i)
     
def my_generator():
    yield

gen = my_generator()
print(next(gen)) # StopIteration


print("fib.....")
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib_generator()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3

for _ in range(10):
    print(next(gen)) # 5-377

for _ in range(10):
    print(next(gen)) # 610-46368


    