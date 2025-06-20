from lldPython.design_patterns.stratergyModified.factory.sortingFactory import SortingFactory
from lldPython.design_patterns.stratergyModified.bubbleSort import BubbleSort
from lldPython.design_patterns.stratergyModified.quickSort import QuickSort
from lldPython.design_patterns.stratergyModified.mergeSort import MergeSort

# # in casse directly call to main.py
# class Sorter:
#     def sort_data(self, data, algorithm):
#         if algorithm == "bubble":
#             sorter = BubbleSort()
#         elif algorithm == "quick":
#             sorter = QuickSort()
#         elif algorithm == "merge":
#             sorter = MergeSort()
#         else:
#             raise ValueError(f"Unknown sorting algorithm type: {algorithm}")
#         return sorter.sort(data)

# in case of strategy pattern, we can use the factory to get the sorting algorithm
class Sorter:
    def sort_data(self, data, algorithm):
        strategy = SortingFactory.get_sorting_algorithm(algorithm)
        return strategy.sort(data) if strategy else None