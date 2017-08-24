def add(s, r):
    if r:
        s.add(r.val)
        add(s, r.left)
        add(s, r.right)
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        add(s, root)
        for i in s:
            if (k-i) in s and i+i != k:
                return True
        return False
