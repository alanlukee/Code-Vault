# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):  #n = 5
        i = 1
        j = n
        while(i<=j):
            mid = (i+j)//2
            if isBadVersion(mid)==False:
                i =mid+1
            else:
                j = mid -1
        return i
        #[1,2,3,4,5]  -> [good,good, good, bad,bad]