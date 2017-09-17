class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        u, d = 0, 0
        for c in s:
            if c == '(':
                u += 1
                d += 1
                continue
            if c == ')':
                u -= 1
                d -= 1
                if u < 0:
                    return False
                if d < 0:
                    d = 0
                continue
            u += 1
            d -= 1
            if d < 0:
                d = 0
        return d == 0
