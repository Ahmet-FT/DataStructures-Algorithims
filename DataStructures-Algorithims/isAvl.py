class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):

        sol = self.find_height(root.left)
        sag = self.find_height(root.right)

        avl = sol - sag

        print(f"sol: {sol} sag: {sag}")

        if avl < -1 or 1 < avl:
            print(avl)
            return False
        else:
            print(avl)
            return True

    def find_height(cls, root, i = -1):

        if root is None:
            return i
        i += 1
        sol = cls.find_height(root.left, i)
        sag = cls.find_height(root.right, i)

        if sol < sag:
            #print(f"ağacın sagı: {sag} solu: {sol}")
            return sag
        else:
            #print(f"ağacın sagı: {sag} solu: {sol}")
            return sol
        


A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)
F = TreeNode(17)

A.left = B
A.right = C
C.left = D
C.right = E
E.right = F

print(Solution().isBalanced(A))
        



        