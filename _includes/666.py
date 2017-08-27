def maketree(level, l, d):
    if not level:
        return None
    r = TreeNode(None)
    r.left = maketree(level-1, l*2, d)
    r.right = maketree(level-1, l*2+1, d)
    d[str(5-level)+str(l+1)] = r
    return r

def calc(r):
    if r is None:
        return 0, 0
    if r.val is None:
        return 0, 0
    a, b = calc(r.left)
    c, d = calc(r.right)
    if b == d == 0:
        b = 1
    return a+c+r.val*(b+d), b+d

class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        d = {}
        r = maketree(4, 0, d)
        for i in nums:
            a, b, c = str(i)
            d[a+b].val = int(c)
        return calc(r)[0]
