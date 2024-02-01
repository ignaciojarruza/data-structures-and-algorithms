# Python arrays are dynamic by default, but this is an example of resizing and the process
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.array = [0] * 2  # standard capacity of 2

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.capacity == self.length:
            self.resize()
        else:
            self.array[self.length] = n
            self.length += 1

    # resize array when capacity is reached
    def resize(self):
        self.capacity = 2 * self.capacity
        newArray = [0] * self.capacity

        for i in range(self.array):
            newArray[i] = self.array[i]
        self.array = newArray

    # remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1

    # get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.array[i]
        # out of bounds exception

    # insert n at i-th index
    def insert(self, i, n):
        if i < self.length:
            self.array[i] = n
        # out of bounds exception

    def print(self):
        for i in range(self.length):
            print(self.array[i])
        print()
