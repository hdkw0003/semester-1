# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self = [x for x in filename]
        

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        print(len(self))

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        print(self[index])
        

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        sum(self) / len(self)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        if (len(sorted.self) % 2) = 0:
            median = (self[(len(self) - 2) / 2] + self[len(self) / 2]) / 2
            return median
        elif (len(sorted.self) % 2) = 1:
            median = self[len(self) - 1]
            return median

