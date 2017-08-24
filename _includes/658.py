from bisect import bisect
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = bisect(arr, x)
        left, right = i-1, i
        d = 0
        results = []
        for i in range(k):
            if left >= 0:
                lv = arr[left]
                ld = x - lv
            else:
                ld = 100000
            if right < len(arr):
                rv = arr[right]
                rd = rv - x
            else:
                rd = 100000
            if ld <= rd:
                results.append(lv)
                left -= 1
            else:
                results.append(rv)
                right += 1
        results.sort()
        return results
