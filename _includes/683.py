class Part:
    def __init__(self, n, s, d, l, r):
        self.n = n
        self.s = s
        self.d = d
        self.l = l
        self.r = r
        self.lc = None
        self.rc = None
        if r != n + 1:
            s.setdefault(r - d - 1, 0)
            s[r - d - 1] += 1
        if l:
            s.setdefault(d - l - 1, 0)
            s[d - l - 1] += 1
    def part(self, p):
        if p > self.d:
            if self.rc:
                return self.rc.part(p)
            self.rc = Part(self.n, self.s, p, self.d, self.r)
            if self.r != self.n + 1:
                self.s[self.r - self.d - 1] -= 1
        else:
            if self.lc:
                return self.lc.part(p)
            self.lc = Part(self.n, self.s, p, self.l, self.d)
            if self.l:
                self.s[self.d - self.l - 1] -= 1

class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        if n < 2:
            return -1
        s = {}
        parts = Part(n, s, flowers[0], 0, n+1)
        for d in range(1, n):
            if k in s and s[k]:
                return d
            parts.part(flowers[d])
        return -1
