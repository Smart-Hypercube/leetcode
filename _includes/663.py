def scan(r, s, canadd=False):
    if not r:
        return 0
    v = r.val
    v += scan(r.left, s, True)
    v += scan(r.right, s, True)
    if canadd:
        s.add(v)
    return v

class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = set()
        s = scan(root, values)
        if s & 1:
            return False
        return (s//2) in values
