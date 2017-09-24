class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nt = int(time[0]), int(time[1]), int(time[3]), int(time[4])
        ts = {nt}
        ds = set(nt)
        for d1 in ds:
            if d1 > 2:
                continue
            for d3 in ds:
                if d3 > 5:
                    continue
                for d2 in ds:
                    if d1*10 + d2 > 23:
                        continue
                    for d4 in ds:
                        ts.add((d1, d2, d3, d4))
        ts = list(ts)
        ts.sort()
        i = ts.index(nt)
        if i == len(ts) - 1:
            return '%s%s:%s%s' % ts[0]
        return '%s%s:%s%s' % ts[i+1]
