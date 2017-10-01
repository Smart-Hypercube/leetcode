# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def calc(n, v, le):
    if not n:
        return 0, 0
    if v == n.val:
        l, ll = calc(n.left, v, le+1)
        r, rr = calc(n.right, v, le+1)
        return 1 + max(l, r), max(l+r, ll, rr)
    l, ll = calc(n.left, n.val, le+1)
    r, rr = calc(n.right, n.val, le+1)
    return 0, max(l+r, ll, rr)

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return calc(root, None, 0)[1]
