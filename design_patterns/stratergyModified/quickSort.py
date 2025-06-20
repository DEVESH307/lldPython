from lldPython.design_patterns.stratergyModified.sorting import Sorting

class QuickSort(Sorting):
    def sort(self, data):
        """
        Sorts the data in ascending order using quick sort algorithm.
        :param data: list of integers to be sorted
        :return: sorted data
        """
        # print("Quick Sort Algorithm")
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)
