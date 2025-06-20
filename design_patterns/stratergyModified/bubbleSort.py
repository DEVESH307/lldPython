from lldPython.design_patterns.stratergyModified.sorting import Sorting

class BubbleSort(Sorting):
    def sort(self, data):
        """
        Sorts the data in ascending order using bubble sort algorithm.
        :param data: list of integers to be sorted
        :return: sorted data
        """

        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data
