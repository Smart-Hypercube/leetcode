def wobt(root, m, depth=0, position=0):
    if not root:
        return
    l, r = m.get(depth, (position, position))
    m[depth] = min(l, position), max(r, position)
    wobt(root.left, m, depth+1, position<<1)
    wobt(root.right, m, depth+1, (position<<1)+1)

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = {}
        wobt(root, d)
        l = []
        for k in d:
            l.append(d[k][1] - d[k][0])
        return max(l) + 1
