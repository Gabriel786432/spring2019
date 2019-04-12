operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def eval(self, node=None):
        if node is None: return self.eval(self) # for node.eval()

        # Alternative:
        # isLeaf = node.right is None and node.left is None
        if type(node.data) == int or type(node.data) == float:
            return node.data

        value_left = self.eval(node.left)
        value_right = self.eval(node.right)
        return node.data( value_left, value_right )

# Expression for: "4 / 2 + 3 * 4"
root = Node(operations['+'], left=Node(operations['-'], left=Node(operations['+'],
    left=Node(operations['*'], left=Node(3), right=Node(1)),
    right=Node(operations['/'], left=Node(6), right=Node(3))), right=Node(3)), right=Node(5))
total = root.eval()
print(total)
