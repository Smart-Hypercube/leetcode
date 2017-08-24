class Solution:
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        cost = [-1] * len(A) + [0] + [-1] * (B-1)
        path = [()] * len(A) + [()] *B
        for i in range(len(A)):
            if A[i] == -1:
                cost[i] = -1
            else:
                try:
                    c, p = min(((cost[i-j], path[i-j]+(i,)) for j in range(1, B+1) if cost[i-j] != -1))
                    cost[i] = c+A[i]
                    path[i] = p
                except ValueError:
                    cost[i] = -1
                    path[i] = ()
        return [i+1 for i in path[len(A)-1]]
