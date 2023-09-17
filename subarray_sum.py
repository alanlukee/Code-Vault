arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
start = 0
end = 0
current_sum = arr[start]
while(end<len(arr)):
    if (current_sum == target_sum):
        print(start,end)
        break
    if (current_sum >target_sum):
        current_sum = current_sum - arr[start]
        start = start+1
    else:
        end= end+1
        if end<len(arr):
            current_sum = current_sum + arr[end]
print(arr[start:end+1])