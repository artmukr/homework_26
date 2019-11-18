class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def push(self, value, root=None):
        if root is None:
            root = self.root
        if not self.root:
            self.root = BSTNode(value)
            return

        if value <= root.value:
            if not root.left:
                root.left = BSTNode(value)
            else:
                self.push(value, root.left)
        else:
            if not root.right:
                root.right = BSTNode(value)
            else:
                self.push(value, root.right)

    def delete(self, value, root=None):

        if root is None:
            root = self.root

        if value < root.value:
            if root.left.value == value:
                root.left = root.left.right
            elif value != root.left.value:
                self.delete(value, root.left)
            else:
                return

        elif value > root.value:
            if root.right.value == value:
                root.right = root.right.right
            elif value != root.right.value:
                self.delete(value, root.right)
            else:
                return

    def max_v(self, root=None, max_value=int):
        if root is None:
            root = self.root
        if root.right:
            max_value = root.right.value
            print('test')
            self.max_v(root.right, max_value)
        else:
            return max_value

    def min_v(self, root=None, min_value=int):
        if root is None:
            root = self.root
            min_value = self.root.value
        if root.left:
            print('test')
            min_value = root.left.value
            self.min_v(root.left, min_value)
        else:
            return min_value


ob1 = BST()

ob1.push(1)
ob1.push(3)
ob1.push(4)
ob1.push(2)
ob1.push(5)
ob1.push(6)
ob1.push(7)
ob1.push(0)


print(ob1.root.value, ob1.root.right.value,
      ob1.root.right.left.value, ob1.root.right.right.value,
      ob1.root.right.right.right.value,
      ob1.root.right.right.right.right.value,
      ob1.root.right.right.right.right.right.value)

ob1.delete(5)

print(ob1.root.value, ob1.root.right.value,
      ob1.root.right.left.value, ob1.root.right.right.value,
      ob1.root.right.right.right.value,
      ob1.root.right.right.right.right.value)

print(ob1.max_v())
print(ob1.min_v())
