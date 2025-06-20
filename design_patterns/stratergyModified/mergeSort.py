from lldPython.design_patterns.stratergy.Sorting import Sorting

class MergeSort(Sorting):
    def sort(self, data):
        """
        Sorts the data in ascending order using merge sort algorithm.
        :param data: list of integers to be sorted
        :return: sorted data
        """
        # print("Merge Sort Algorithm")
        if len(data) > 1:
            mid = len(data) // 2
            l = data[:mid]
            r = data[mid:]
            self.sort(l)
            self.sort(r)
            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    data[k] = l[i]
                    i += 1
                else:
                    data[k] = r[j]
                    j += 1
                k += 1
            while i < len(l):
                data[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                data[k] = r[j]
                j += 1
                k += 1
        return data

