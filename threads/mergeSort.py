# # 0. Merge Sort with Parallel Processing(Original Code)
# import concurrent.futures
# import random
# import time


# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = mergeSort(left)
#     right = mergeSort(right)
#     return merge(left, right)


# def merge(leftarr, rightarr):
#     result = []
#     left = 0
#     right = 0

#     while left < len(leftarr) and right < len(rightarr):
#         if leftarr[left] <= rightarr[right]:
#             result.append(leftarr[left])
#             left += 1
#         else:
#             result.append(rightarr[right])
#             right += 1
#     result.extend(leftarr[left:])
#     result.extend(rightarr[right:])
#     return result


# def parllel_merge_sort(arr, maxWorkers):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers) as executor:
#         left_future = executor.submit(mergeSort, left)
#         right_future = executor.submit(mergeSort, right)

#         left_arr = left_future.result()
#         right_arr = right_future.result()

#     return  merge(left_arr, right_arr)


# if __name__ == "__main__":
#     arr = [random.randint(0, 100) for i in range(5000000)]

#     # Single-threaded merge sort
#     start_time = time.time()
#     sorted_array_single_thread = mergeSort(arr)
#     end_time = time.time()
#     single_thread_duration = end_time - start_time

#     print(f"Execution time: {end_time - start_time}")

#     # print(f"Single-threaded sorted array: {sorted_array_single_thread}")
#     start_time = time.time()

#     max_workers = 4
#     sorted_arr = parllel_merge_sort(arr, max_workers)
#     # print(sorted_arr)
#     end_time = time.time()

#     print(f"Execution time: {end_time - start_time}")




# 1. Merge Sort with Parallel Processing (Modified Code)
import concurrent.futures
import random
import time

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(leftarr, rightarr):
    result = []
    left = 0
    right = 0

    while left < len(leftarr) and right < len(rightarr):
        if leftarr[left] <= rightarr[right]:
            result.append(leftarr[left])
            left += 1
        else:
            result.append(rightarr[right])
            right += 1
    result.extend(leftarr[left:])
    result.extend(rightarr[right:])
    return result


def parallel_merge_sort(arr, maxWorkers):
    """Sorts an array using merge sort with parallel processing."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
        # output = 0.004799604415893555 (range=100)
        # output = 22.229393005371094 (range=5000000)
    with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers) as executor:
        # output = 0.16916990280151367 (range=100)
        # output = 13.638299703598022 (range=5000000)
        left_future = executor.submit(mergeSort, left)
        right_future = executor.submit(mergeSort, right)

        left_arr = left_future.result()
        right_arr = right_future.result()
        
    return merge(left_arr, right_arr)
    

if __name__ == "__main__":
    start_time = time.time()
    
    # arr = [random.randint(0, 100) for i in range(100)]
    arr = [random.randint(0, 100) for i in range(5000000)]
    # max_workers = 1
    max_workers = 2
    # max_workers = 3 
    # max_workers = 4
    sorted_arr = parallel_merge_sort(arr, max_workers)
    end_time = time.time()
    # print(f"Sorted array: {sorted_arr}")
    print(end_time - start_time)
    
    
    
# ⚙️ Parallel Merge Sort and max_workers=2
# When you set max_workers=2 (e.g., in Python's concurrent.futures), it means:

# Only two threads/processes will work concurrently.

# One handles the left half, the other the right half.

# That fits naturally with the recursive binary structure of merge sort:

# css
# Copy
# Edit
#                 A
#               /   \
#             L       R
# Here, 2 workers are enough to process L and R in parallel.

# ❓ Why Not max_workers > 2?
# 🧠 1. Merge Sort is Binary
# At each level, you only split into 2 halves.

# Spawning more workers than halves causes idle threads (no gain).

# 🧱 2. Merge is Sequential (usually)
# Even if sorting is parallel, the merge step often requires sequential processing.

# You can parallelize it, but it’s complex and often not worth it for small arrays.

# 🧵 3. Thread/Process Overhead
# Spawning many threads/processes increases overhead (context switching, memory).

# This can slow down rather than help, especially on small inputs.

# 🎯 4. Optimal Parallelization
# Using more than 2 workers might only be helpful at higher levels of recursion.

# You can parallelize top N levels only, and let deeper calls run sequentially.

# ✅ When to Use More Workers
# If you want to use more cores efficiently, you need:

# A parallel task queue

# A depth-limited parallelism (e.g., only parallelize the first few levels of recursion)

# A work-stealing scheduler (used in frameworks like Java’s ForkJoinPool)

# In those cases, max_workers > 2 can help. But naive recursion with >2 workers leads to poor resource usage.

# 🧩 Summary
# Reason	Why Only 2 Workers
# Binary recursion	Only two halves to split
# Merge is usually sequential	Can’t fully parallelize
# Too many threads = overhead	Slower performance
# Diminishing returns	Not worth >2 on small inputs