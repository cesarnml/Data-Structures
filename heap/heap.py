class Heap:
    def __init__(self):
        self.storage = []
    """
    Add value to the end of array.
    Then use _bubble_up to move value to correct index
    """

    def insert(self, value):
        last = len(self.storage) - 1
        self.storage.append(value)
        self._bubble_up(last)
    """
    Store max_value
    Copy last element into first index
    Delete last element
    If the array isn't empty; call _sift_down to find
    correct position for new top value
    Return deleted max_value
    """

    def delete(self):
        last = len(self.storage) - 1
        max_value = self.storage[0]
        self.storage[0] = self.storage[last]
        self.storage.pop()
        if len(self.storage):
            self._sift_down(0)
        return max_value

    # max_value always at index 0
    def get_max(self):
        return self.storage[0]

    # use built-in len function to get size of array
    def get_size(self):
        return len(self.storage)
    """
    While there is a parent index,
    Check if parent value < index value
    If yes => swap items ... set new index = parent index ... iterate up one level
    If no => breakout of while loop, item in proper position
    """

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self.storage[parent] < self.storage[index]:
                self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
                index = parent
            else:
                break

    """
    While there is still a child_index in the array for current parent index
    If right_child index > last, no right_child exist; left_child must be maximum value
    Otherwise, index has two children => check which is greater
    max_child => set to biggest child index
    If value at max_child > value at index => swap and set new index = max_child => iterate one level down
    Otherwise, value at index in correct position break out of while loop.
    """

    def _sift_down(self, index):
        last = len(self.storage) - 1
        while index * 2 + 1 <= last:
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            if right_child > last:
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
