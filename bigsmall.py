arr = [1,2,3,4,5,6,7,8,9]
#output => [7,1,6,2,5,3,4]
s =0
l = len(arr) - 1
temp = []
flag = True
for i in range(len(arr)):
    if flag is True:
        temp.append(arr[l])
        l = l-1
    else:
        temp.append(arr[s])
        s = s+1
    flag = not flag
print(temp)
