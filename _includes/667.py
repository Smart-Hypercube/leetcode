class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        r = [i for i in range(1, n-k+1)]
        s = r[-1]
        d = 1
        while len(r) < n:
            s += d*k
            r.append(s)
            d = -d
            k -= 1
        return r
