print("Enter arr:")
arr = list(map(int, input().split()))
print("enter position")
input1 = int(input())
temp = arr[input1 - 1] 

while(input1>0):
    arr[input1 - 1] = arr[input1 - 1 -1]
    input1 = input1 - 1
arr[0] = temp
print(arr)
