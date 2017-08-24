class Solution:
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ''
        while n >= 9:
            s += str(n % 9)
            n //= 9
        s += str(n)
        return int(''.join(reversed(s)))
