class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ends = {}
        for i in nums:
            ends.setdefault(i, [])
            if ends[i]:
                m = 0
                l = len(ends[i][0])
                for j in range(len(ends[i])):
                    ll = len(ends[i][j])
                    if ll < l:
                        m, l = j, ll
                l = ends[i].pop(m)
            else:
                l = []
            l.append(i)
            ends.setdefault(i+1, [])
            ends[i+1].append(l)
        for k in ends:
            for l in ends[k]:
                if len(l) < 3:
                    return False
        return True
