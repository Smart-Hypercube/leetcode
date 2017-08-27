def oub(m, n, v):
    """order's upper boundary"""
    r = 0
    i = 1
    mn = min(m, n)
    while i*i <= v and i <= mn:
        t = v // i
        r += min(t, m) - i + min(t, n) - i + 1
        i += 1
    return r

def bsearch(m, n, k, l, r):
    mid = (l + r) >> 1
    o = oub(m, n, mid)
    if o < k:
        return bsearch(m, n, k, mid+1, r)
    if o-mid >= k or oub(m, n, mid-1) >= k:
        return bsearch(m, n, k, l, mid)
    else:
        return mid

class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        return bsearch(m, n, k, 1, m*n+1)
