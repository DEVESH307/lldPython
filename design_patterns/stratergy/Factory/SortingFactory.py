from design_patterns.stratergy.BubbleSort import BubbleSort
from design_patterns.stratergy.MergeSort import MergeSort
from design_patterns.stratergy.quickSort import QuickSort


class SortingFactory:
    @staticmethod
    def getSortingObj(algo):
        if algo == "Bubble Sort":
            return BubbleSort()
        if algo == "Quick":
            return QuickSort()
        if algo == "Merge":
            return MergeSort()
