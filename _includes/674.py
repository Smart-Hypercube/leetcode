class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m = 0
        length = 0
        last = nums[0] - 1
        for i in nums:
            if i > last:
                length += 1
                last = i
            else:
                m = max(m, length)
                length = 1
                last = i
        return max(m, length)
