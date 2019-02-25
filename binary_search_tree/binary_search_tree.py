class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Empty Binary Search Tree
        if self.value is None:
            self.value = value
        else:
            # If value greater than or equal to self.value, insert in right branch
            if self.value <= value:
                # If at a leaf, insert BST node with given value
                if self.right is None:
                    self.right = BinarySearchTree(value)
                # Else recurse insert method on self.right
                else:
                    self.right.insert(value)
            # Analogues logic for value less than self.value, insert in left branch
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)

    def contains(self, target):
        if self.value is None:
            return False
        if self.value == target:
            return True
        while self.right is not None:
            print('in 3')
            self.right.contains(target)
        while self.left is not None:
            print('in 4')
            self.left.contains(target)
        return False

    def get_max(self):
        pass
