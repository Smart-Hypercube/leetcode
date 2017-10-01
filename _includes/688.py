cache = {}

def calc(N, K, r, c):
    if r not in range(N):
        return 0
    if c not in range(N):
        return 0
    if not K:
        return 1
    r = min(r, N-1-r)
    c = min(c, N-1-c)
    if (N, K, r, c) in cache:
        return cache[N, K, r, c]
    p = 0
    p += calc(N, K-1, r-1, c-2)
    p += calc(N, K-1, r-2, c-1)
    p += calc(N, K-1, r-1, c+2)
    p += calc(N, K-1, r-2, c+1)
    p += calc(N, K-1, r+1, c-2)
    p += calc(N, K-1, r+2, c-1)
    p += calc(N, K-1, r+1, c+2)
    p += calc(N, K-1, r+2, c+1)
    cache[N, K, r, c] = p / 8
    return p / 8

class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        return calc(N, K, r, c)
