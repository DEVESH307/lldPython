from lldPython.design_patterns.stratergyModified.bubbleSort import BubbleSort
from lldPython.design_patterns.stratergyModified.quickSort import QuickSort
from lldPython.design_patterns.stratergyModified.mergeSort import MergeSort


class SortingFactory:
    @staticmethod
    def getSortingObj(algo):
        if algo == "Bubble Sort":
            return BubbleSort()
        if algo == "Quick":
            return QuickSort()
        if algo == "Merge":
            return MergeSort()
