class Node:
    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.color = color

class MyTree:
    def __init__(self):
        self.root = None
        self.RED = True
        self.BLACK = False

    def is_red(self, x):
        if x is None:
            return False
        return x.color == MyTree.RED
    
    def __put(self, h, key, val):
        if h is None:
            return Node(key, val, MyTree.RED, 1)
        if h.key > key:
            h.left = self.__put(h.left, key, val)
        if h.key < key:
            h.rigth = self.__put(h.right, key, val)

        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.rigth):
            self.flip_colors(h)

    def put(self, key, val):
        self.root = self.__put(self.root, key, val)
        self.root.color = MyTree.BLACK

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = MyTree.RED
        return x
    
    def rotate_rigth(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = MyTree.RED
        return x
    
    def flip_colors(self, h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right = not h.right.color

    def is23(self):
        return self.__is23(self.root)
    
    def __is23(self, node):
        if node is None:
            return True
        if self.is_red(node.right):
            return False
        if node != self.root and self.is_red(node) and self.is_red(node.left):
            return False
        return self.__is23(node.left) and self.__is23(node.right)

def main():
    mt = MyTree()
    nodes = int(input())
    for i in range(nodes):
        mt.put(int(input(), ""))
    print(mt.is23())

if __name__ == '__main__':
    main()