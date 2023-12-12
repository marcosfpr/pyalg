class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def height(self):
        if self.left is None and self.right is None:
            return 0

        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0

        return max(left, right) + 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)

    def height(self):
        return self.root.height()

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)

    def inorder(self):
        elements = []
        self._inorder(self.root, elements)
        return elements

    def _inorder(self, node, elements):
        if node is not None:
            self._inorder(node.left, elements)
            elements.append(node.value)
            self._inorder(node.right, elements)

    def postorder(self):
        elements = []
        self._postorder(self.root, elements)
        return elements

    def _postorder(self, node, elements):
        if node is not None:
            self._postorder(node.left, elements)
            self._postorder(node.right, elements)
            elements.append(node.value)

    def preorder(self):
        elements = []
        self._preorder(self.root, elements)
        return elements

    def _preorder(self, node, elements):
        if node is not None:
            elements.append(node.value)
            self._preorder(node.left, elements)
            self._preorder(node.right, elements)


if __name__ == "__main__":
    import random
    from copy import copy

    arr = [1, 2, 4, 7, 10, 15, 20, 47, 50, 92, 101]

    random.shuffle(arr)

    tree = BST()
    for elem in arr:
        tree.insert(elem)

    print(f"In-order: {tree.inorder()}")
    print(f"Post-order: {tree.postorder()}")
    print(f"Pre-order: {tree.preorder()}")

    print(f"Tree height: {tree.height()}")
