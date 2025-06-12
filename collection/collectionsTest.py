# l = list[]
# l = list[1,2,3,4,5]
# print(l)

# for i in l:
#     print(i)

# immutable data structure
t = tuple([1, 2, 3, 4, 5])
# print(t)

# for i in t:
#     print(i)

# unpacking a tuple
# a,b,c,d,e = t
# print(a, b, c, d, e)

# unordered collection of unique elements
# s = set([1, 2, 3, 4, 5])

# # for i in s:
# #     print(i)

# # s.remove(1)
# # print(s)

# my_set = {1, 2, 3, 4, 5, 5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5}

# my_set.remove(1)
# # my_set.remove(1) # keyerror
# # print(my_set)

# another_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # union of two sets 
# union_set = my_set.union(another_set)
# print(union_set)

# # intersection of two sets
# intersection_set = my_set.intersection(another_set)
# print(intersection_set)

# # difference of two sets
# difference_set = another_set.difference(my_set)
# print(difference_set)

# frozen set immutable set
# frozen_set = frozenset([1, 2, 3, 4, 5])
# # print(frozen_set)

# frozen_set.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen_set.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'
# frozen_set.clear()  # AttributeError: 'frozenset' object has no attribute 'clear'
# print(frozen_set)


# # dictionary defination: Hash Map
# my_dict = dict()
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# print(my_dict['age'])  # Accessing value by key
# print(my_dict.get('name'))  # Accessing value using get method

# print(my_dict['a'])  # KeyError: 'a' if key does not exist
# print(my_dict.get('a'))  # Returns None if key does not exist

# print(my_dict.get('a', 'Key not found'))  # Returns 'Key not found' if key does not exist

# my_dict['age'] = 31  # Updating value
# my_dict['country'] = 'USA'  # Adding new key-value pair

# # Nested dictionary
# nested_dict = {
#     'person1': {'name': 'Alice', 'age': 25},
#     'person2': {'name': 'Bob', 'age': 30}
# }

# # Accessing nested dictionary values
# print(nested_dict['person1']['name'])  # Output: Alice
# print(nested_dict.get('person2', {}).get('age', 'Not Found'))  # Output: 30

# # Triple nested dictionary
# triple_nested_dict = {
#     'group1': {
#         'person1': {'name': 'Alice', 'age': 25},
#         'person2': {'name': 'Bob', 'age': 30}
#     },
#     'group2': {
#         'person3': {'name': 'Charlie', 'age': 35},
#         'person4': {'name': 'David', 'age': 40}
#     }
# }

# # Accessing triple nested dictionary values
# print(triple_nested_dict['group1']['person1']['name'])  # Output: Alice
# print(triple_nested_dict.get('group2', {}).get('person3', {}).get('name', 'Not Found'))  # Output: Charlie

# # Iterating through dictionary keys and values
# for key, value in my_dict.items():
#     print(f"{key}: {value}")


# # Default dictionary
# from collections import defaultdict

# default_dict = defaultdict(lambda: 2)
# default_dict['a'] = 1
# print(default_dict['a'])  # Output: 1
# print(default_dict['b'])  # Output: 2 (default value since 'b' is not set)

# # Counter: Count occurrences of elements in a list
# lst = [1, 2, 3, 4, 5, 1, 4, 2, 7, 4, 1, 4, 5, 2, 4]
# from collections import Counter
# # Count occurrences of each element in the list
# count_dict = Counter(lst)
# print(count_dict)  # Output: Counter({4: 3, 1: 2, 2: 2, 3: 1, 5: 1, 7: 1})

# # Accessing count of a specific element
# print(count_dict[4])  # Output: 5
# # Accessing count of a non-existing element
# print(count_dict[10])  # Output: 0 (default value for non-existing keys) 

# # Deque: Double-ended queue
# from collections import deque
# # Create a deque
# deq = deque([1, 2, 3, 4, 5])
# # Append elements to the right
# deq.append(6)
# # Append elements to the left
# deq.appendleft(0)
# # Pop elements from the right
# deq.pop()
# # Pop elements from the left
# deq.popleft()
# # Print the deque
# print(deq)  # Output: deque([0, 1, 2, 3, 4, 5])
# # Rotate the deque
# deq.rotate(2)  # Rotate right by 2 positions
# print(deq)  # Output: deque([4, 5, 0, 1, 2, 3])
# # Rotate the deque left by 2 positions
# deq.rotate(-2)
# print(deq)  # Output: deque([0, 1, 2, 3, 4, 5])
# # Clear the deque
# deq.clear()
# # Print the cleared deque
# print(deq)  # Output: deque([])
# # Check if the deque is empty
# print(len(deq) == 0)  # Output: True (deque is empty)
# # Check if the deque is not empty
# print(len(deq) != 0)  # Output: False (deque is empty)
# # Check if the deque contains a specific element
# print(1 in deq)  # Output: False (deque is empty)
# # Check if the deque does not contain a specific element
# print(1 not in deq)  # Output: True (deque is empty)
# # Check the length of the deque
# print(len(deq))  # Output: 0 (deque is empty)
# # Check the first element of the deque
# print(deq[0])  # IndexError: deque index out of range (deque is empty)
# # Check the last element of the deque
# print(deq[-1])  # IndexError: deque index out of range (deque is empty)


# OrderedDict: Dictionary that remembers the order of insertion
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
# Print the ordered dictionary
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Accessing elements in the ordered dictionary
print(od['a'])

# update ordered dictionary
od['d'] = 4
print(od)
