class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        m = [[1] * (l + 1) for i in range(l + 1)]
        for i in range(l + 1):
            m[i][i] = 0
        for length in range(1, l + 1):
            for offset in range(l - length + 1):
                m[offset][offset + length] = m[offset + 1][offset + length]
                m[offset][offset + length] = min(
                    m[offset + 1][offset + i] + m[offset + i][offset + length]
                    for i in range(length)
                    if s[offset] == s[offset + i])
        return m[0][l]
