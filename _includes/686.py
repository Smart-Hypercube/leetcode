class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = (len(B) - 1) // len(A) + 1
        if B in A * n:
            return n
        if B in A * (n + 1):
            return n + 1
        return -1
