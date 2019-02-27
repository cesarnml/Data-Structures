class Heap:
    def __init__(self):
        self.storage = []

    # Add value to the end of array.
    # Then use _bubble_up to move value to correct index
    def insert(self, value):
        last = len(self.storage) - 1
        self.storage.append(value)
        self._bubble_up(last)

    # Store max_value
    # Copy last element into first index
    # Delete last element
    # If the array isn't empty; call _sift_down to find
    # correct position for new top value
    # Return deleted value
    def delete(self):
        last = len(self.storage) - 1
        max_value = self.storage[0]
        self.storage[0] = self.storage[last]
        del self.storage[last]
        if len(self.storage):
            self._sift_down(0)
        return max_value

    # max_value always at index 0
    def get_max(self):
        return self.storage[0]

    # use built-in len function to get size of array
    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):

        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self.storage[parent] < self.storage[index]:
                self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
            index = parent

    def _sift_down(self, index):
        last = len(self.storage) - 1
        while index * 2 + 1 <= last:
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            if index * 2 + 2 > last:
                max_child = left_child
            else:
                if self.storage[left_child] > self.storage[right_child]:
                    max_child = left_child
                else:
                    max_child = right_child
            if self.storage[index] < self.storage[max_child]:
                self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
                index = max_child
            else:
                break
