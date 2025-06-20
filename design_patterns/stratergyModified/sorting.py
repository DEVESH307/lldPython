from abc import ABC, abstractmethod

class Sorting:
    @abstractmethod
    def sort(self, data):
        """
        Sorts the data in ascending order.
        :return: sorted data
        """
        pass