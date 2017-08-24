class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        columns = len(M[0]) if rows else 0
        r = []
        for i in range(rows):
            r.append([0] * columns)
        for x in range(rows):
            for y in range(columns):
                cs = []
                if x-1 in range(rows):
                    if y-1 in range(columns):
                        cs.append(M[x-1][y-1])
                    cs.append(M[x-1][y])
                    if y+1 in range(columns):
                        cs.append(M[x-1][y+1])
                if y-1 in range(columns):
                    cs.append(M[x][y-1])
                cs.append(M[x][y])
                if y+1 in range(columns):
                    cs.append(M[x][y+1])
                if x+1 in range(rows):
                    if y-1 in range(columns):
                        cs.append(M[x+1][y-1])
                    cs.append(M[x+1][y])
                    if y+1 in range(columns):
                        cs.append(M[x+1][y+1])
                r[x][y] = sum(cs) // len(cs)
        return r
