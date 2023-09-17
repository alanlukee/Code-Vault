def sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums) // 2
    left = sort(nums[:mid])
    right = sort(nums[mid:])

    return merge(left,right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [12, 5, 9, 23, 8, 4, 17]
sorted_arr = sort(arr)
print(sorted_arr)

