# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def trim(n, l, r):
    if not n:
        return
    if l <= n.val <= r:
        n.left = trim(n.left, l, r)
        n.right = trim(n.right, l, r)
        return n
    if n.val < l:
        return trim(n.right, l, r)
    else:
        return trim(n.left, l, r)

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        return trim(root, L, R)
