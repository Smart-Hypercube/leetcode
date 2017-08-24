class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        t, l = 0, 0
        dt = {'U': -1, 'D': 1}
        dl = {'L': -1, 'R': 1}
        for c in moves:
            t += dt.get(c, 0)
            l += dl.get(c, 0)
        return t == l == 0
