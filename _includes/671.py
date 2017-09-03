# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def add2set(n, s):
    if n:
        s.add(n.val)
        add2set(n.left, s)
        add2set(n.right, s)

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = set()
        add2set(root, s)
        try:
            s.remove(min(s))
            return min(s)
        except:
            return -1
