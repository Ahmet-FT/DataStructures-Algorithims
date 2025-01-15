class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    @classmethod
    def insert(cls, root, value):
        if root is None:
            return Tree(value)
        if value < root.value:
            root.left = cls.insert(root.left, value)
        else:
            root.right = cls.insert(root.right, value)
        return root

    @classmethod
    def search(cls, root, value):
        if root is None:
            return None
        if value < root.value:
            return cls.search(root.left, value)
        if value > root.value:
            return cls.search(root.right, value)
        return root

    @classmethod
    def delete(cls, root, value):
        if root is None:
            return None
        if value < root.value:
            root.left = cls.delete(root.left, value)
        elif value > root.value:
            root.right = cls.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            root.value = cls.min_value(root.right)
            root.right = cls.delete(root.right, root.value)
        return root

    @classmethod
    def print_tree(cls, root):
        if root is None:
            return
        print(root.value)
        cls.print_tree(root.left)
        cls.print_tree(root.right)

    @classmethod
    def min_value(cls, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.value
    @classmethod
    def pre_order(cls, root):
        if root is None:
            return
        print(root.value)
        cls.pre_order(root.left)
        cls.pre_order(root.right)

    @classmethod
    def in_order(cls, root):
        if root is None:
            return
        cls.in_order(root.left)
        print(root.value)
        cls.in_order(root.right)

    @classmethod
    def post_order(cls, root):
        if root is None:
            return
        cls.post_order(root.left)
        cls.post_order(root.right)
        print(root.value)
    
    @classmethod
    def solunSolu(cls, root):
        if root is None:
            return
        pivot = root.left
        root.left = pivot.right
        pivot.right = root
        return cls.pre_order(pivot)

    def SaginSagi(cls, root):
        if root is None:
            return
        
        

    


A = Tree(5)
B = Tree(3)
C = Tree(7)
D = Tree(2)
E = Tree(4)
F = Tree(6)
G = Tree(8)


A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G


A = Tree.insert(A, 9)

#Tree.print_tree(A)

dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mid = len(dizi) // 2

print(dizi[:mid])
print(dizi[(mid + 1):])





