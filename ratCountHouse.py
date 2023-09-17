r = int(input())   #number of cats
unit = int(input()) #amount of food each rat consumes

arr =list(map(int, input().split())) #ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i
# print("unit -> ", unit)
# print("n -> ", n)
# print("arr ->", arr)
if len(arr) ==0:
    print("-1")

totalFood = r*unit
sum = 0
for i in range(len(arr)):

    sum = sum +arr[i]
    if sum>=totalFood:
        print(i+1)
        break
