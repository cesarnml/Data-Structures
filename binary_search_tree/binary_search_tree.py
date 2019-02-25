class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Empty Binary Search Tree
        if self.value is None:
            self.value = value
        if self.value <= value:
            self.right.insert(value)
        if self.value > value:
            self.left.insert(value)
            
    def contains(self, target):
        pass

    def get_max(self):
        pass
