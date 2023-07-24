# class Solution(object):
#     def findMaxAverage(self, nums, k):
        # max_avg = 0
        # for i in range(len(nums)-k+1): #6   0,1,2   k =4   i=0 ,end = 3 , i = 1, end = 4
        #     tot = 0
        #     avg = 0
        #     end = (i+k)-1 
        #     sub_arr = nums[i:end+1]
        #     for j in range(len(nums[i:end+1])):
        #         tot = tot+sub_arr[j]
        #     avg = tot/k
    
        #     if avg > max_avg:
        #         max_avg = avg
        #         #max_arr = sub_arr

        # return max_avg
# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         max_tot = float('-inf')

#         for i in range(len(nums) - k + 1):
#             tot = 0
#             end = (i + k) - 1
#             sub_arr = nums[i:end + 1]
#             tot = sum(sub_arr)
#             max_tot = max(tot, max_tot)

#         return max_tot / float(k)
class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = (window_sum + nums[i]) - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / float(k)




