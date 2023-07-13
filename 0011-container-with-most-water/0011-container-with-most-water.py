class Solution(object):
    def maxArea(self, height):
        # i = 0
        # j = 1
        # maxVol = 0
        # while i < len(height):
        #     if j < len(height):
        #         side = min(height[i], height[j])
        #         maxVol = max(maxVol, side * (j - i))
        #         j += 1
        #     else:
        #         i += 1
        #         j = i + 1
        # return maxVol
        ans, i, j = 0, 0, len(height)-1
        while (i < j):
            if height[i] <= height[j]:
                res = height[i] * (j - i)
                i += 1
            else:
                res = height[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans

