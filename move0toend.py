arr = list(map(int, input().split()))
count = 0
length = len(arr)
for i in range(length):
    if arr[i] !=0:
        arr[count] = arr[i]
        count = count +1

zero_count = length - count
for i in range(-1,-zero_count-1,-1):
    arr[i] = 0
print(arr)