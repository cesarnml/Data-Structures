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
        # Empty BST case
        if self.value is None:
            return False
        # If target == current_node.value => return True
        if self.value == target:
            return True
        # If target >= current_node.value; Search right branch recursively
        # until leaf is found
        if self.value <= target:
            if self.right is None:
                return False
            return self.right.contains(target)
        # Analogues logic, but target < current_node.value; Search left branch recursively
        elif self.value > target:
            if self.left is None:
                return False
            return self.right.contains(target)

    def get_max(self):
        # Empty BST case
        if self.value is None:
            return None
        # If current_node.right is None; no greater value exist; return current_node.value
        if self.right is None:
            return self.value
        else:
            # Else recursively search right branches to find maximum value
            return self.right.get_max()
