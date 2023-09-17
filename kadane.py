#kadanes algorithm
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maxi =float('-inf')
sums = 0
for i in arr:
    sums = sums+i
    if sums>maxi:
        maxi = sums
    if sums<0:
        sums = 0
print(maxi)