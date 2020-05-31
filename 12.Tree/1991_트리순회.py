class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def set_data(self, data):
        self.data = data

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

class Tree:
    def __init__(self, root):
        self.root = root

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def preorder(self, node):
        if (not node == None):
            print(node.data, end='')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if (not node == None):
            self.inorder(node.left)
            print(node.data, end='')
            self.inorder(node.right)

    def postorder(self, node):
        if (not node == None):
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end='')

if __name__ == '__main__':
    n = int(input().strip())
    nodes = []
    for i in range(65, 65 + n):
        nodes.append(Node(chr(i)))

    for i in range(n):
        info = input().strip().split(' ')
        for n in nodes:
            if n.data == info[0]:
                if not info[1] == '.':
                    for m in nodes:
                        if m.data == info[1]:
                            n.set_left(m)
                if not info[2] == '.':
                    for m in nodes:
                        if m.data == info[2]:
                            n.set_right(m)

    tree = Tree(nodes[0])
    tree.preorder(tree.get_root())
    print()
    tree.inorder(tree.get_root())
    print()
    tree.postorder(tree.get_root())
    print()