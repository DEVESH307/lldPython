from lldPython.design_patterns.stratergyModified.client.sorter import Sorter

if __name__ == '__main__':
    sorting = Sorter()
    data = [64, 34, 25, 12, 22, 11, 90]
    # algorithm = "quick"
    # algorithm = "bubble"
    algorithm = "merge"
    sorted_data = sorting.sort_data(data, algorithm)
    print(f"Sorted data using {algorithm} sort: {sorted_data}")
# Output: Sorted data using quick sort: [11, 12, 22, 25, 34, 64, 90]