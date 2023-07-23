import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        # nums.sort()
        # count = 1
        # for i in range(len(nums)-1,-1,-1):
        #     if count == k:
        #         return nums[i]
        #     else:
        #         count = count+1
        
        negated_arr = [-x for x in nums]
        heapq.heapify(negated_arr)
        #print(negated_arr)

        while k > 0:
            largest = -heapq.heappop(negated_arr)

            k -= 1
        return largest
