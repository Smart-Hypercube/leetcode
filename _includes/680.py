def check(s, e):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        if e == 1:
            return False
        return check(s[left+1:right+1], 1) or check(s[left:right], 1)
    return True
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return check(s, 0)
