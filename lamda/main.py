# # 0. Lambda Functions and Functional Prgramming (original code)
# from functools import reduce
# mul = lambda x,y : x*y

# print(mul(2,3))

# is_even = lambda x: x % 2 == 0

# print(is_even(2))

# # MAP, filter, Reduce

# nums = [1,2,3,4,5]

# square = list(map(lambda x: x**2, nums))
# print(square)

# even_filter = list(filter(lambda x: x%2==0, nums))

# print(even_filter)

# nums= [1,2,3,4,5]


# total = reduce(lambda x,y: x+y, nums)

# print(total)


# max_value = reduce(lambda x,y : max(x,y), nums)

# print(max_value)

# print(max(nums))

# words = ["hello", " ", "world"]

# conc = reduce(lambda x,y : x+y, list(filter(lambda word: word!=" ", words)))

# print(conc)



# 1. Lambda Functions and Functional Prgramming (modified code)
from functools import reduce

add = lambda x, y: x+y
print(add(5,7)) # output: 12

mul = lambda x, y: x*y
print(mul(4,3)) # output: 12.

is_even = lambda x: x%2 == 0
print(is_even(6)) # output: True
print(is_even(7)) # output: False

# MAP, filter, Reduce
def find_even(x):
    return x%2 == 0
# map(find_even(10))
# map(lambda x: x%2 == 0)

# map: on list applying logic on each elements
nums = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x: x**2, nums))
print(square)
even_map_bool = list(map(lambda x: x%2 == 0, nums))
print(even_map_bool)

# filter: filtering the data based on logic
even_filter = list(filter(lambda x: x%2 == 0, nums))
print(even_filter)

even_square = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(even_square)

# reduce: narrow down to a single obj
def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

total = add_numbers(nums)
print(total)

total = reduce(lambda x,y: x+y, nums)
print(total)
total = reduce(lambda sum,num: sum+num, nums)
print(total)


def find_max(numbers):
    if not numbers:
        return None  # or raise an error if preferred
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value
max_value = find_max(nums)
print(max_value)

def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers[1:]:
        max_value = max(max_value, num)
    return max_value

max_value = find_max(nums)
print(max_value)

max_value = reduce(lambda x, y: x if x > y else y, nums)
print(max_value)

max_value = reduce(lambda x,y : max(x,y), nums)
print(max_value)
print(max(nums))

words = ["Hello", " ", "World"]
conc = reduce(lambda x,y: x+y, words)
print(conc)

conc = reduce(lambda x,y : x+y, list(filter(lambda word: word!=" ", words)))
print(conc)

