from lldPython.design_patterns.stratergyModified.bubbleSort import BubbleSort
from lldPython.design_patterns.stratergyModified.quickSort import QuickSort
from lldPython.design_patterns.stratergyModified.mergeSort import MergeSort

# in case of factory pattern, we can use the factory to get the sorting algorithm
class SortingFactory:
    @staticmethod
    def get_sorting_algorithm(algorithm_type):
        if algorithm_type == "bubble":
            return BubbleSort()
        elif algorithm_type == "quick":
            return QuickSort()
        elif algorithm_type == "merge":
            return MergeSort()
        else:
            raise ValueError(f"Unknown sorting algorithm type: {algorithm_type}")