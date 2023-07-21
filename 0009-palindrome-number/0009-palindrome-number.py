class Solution(object):
    def isPalindrome(self, x):
        k = str(x)
        if k[::-1]==k:
            return True
        else:
            return False
        