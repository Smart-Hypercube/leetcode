def ms(s):
    if not s:
        return ''
    v = max(s)
    if s[0] == v:
        return s[0] + ms(s[1:])
    m = s.rfind(v)
    return s[m] + s[1:m] + s[0] + s[m+1:]

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(ms(str(num)))
