class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        l = [0] * 10
        s = 0
        for o in ops:
            if o == '+':
                d = l[-1] + l[-2]
                l.append(d)
                s += d
            elif o == 'C':
                s -= l.pop()
            elif o == 'D':
                d = l[-1] * 2
                l.append(d)
                s += d
            else:
                d = int(o)
                l.append(d)
                s += d
        return s
