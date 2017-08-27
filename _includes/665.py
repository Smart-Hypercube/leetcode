class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        chance = True
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if i == 1 or nums[i] >= nums[i-2]:
                    if chance:
                        chance = False
                    else:
                        return False
                else:
                    if i == len(nums)-1:
                        return chance
                    if chance:
                        chance = False
                    else:
                        return False
                    nums[i] = nums[i+1]
                    continue
            i += 1
        return True
