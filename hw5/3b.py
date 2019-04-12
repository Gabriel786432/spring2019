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

class tf:
    def add(right, left):
        return Node(operations['+'], right, left)
    def subtract(right, left):
        return Node(operations['-'], right, left)
    def multiply(right, left):
        return Node(operations['*'], right, left)
    def divide(right, left):
        return Node(operations['/'], right, left)

#For 4 / 2 + 3 * 4
#root = tf.add(tf.divide(Node(4), Node(2)), tf.multiply(Node(3), Node(4)))

#For 3 * 1 + 6 / 3 - 3 + 5
#root = tf.add(tf.subtract(tf.add(tf.multiply(Node(3), Node(1)), tf.divide(Node(6), Node(3))), Node(3)), Node(5))
total = root.eval()

print(total)
