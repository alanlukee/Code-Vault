print("Enter arr:")
arr = list(map(int,input().split()))
print("You have entered an array having length", len(arr))
print("Enter Window Size(plz dont be dumb and put value greater than length):")


window = int(input()) #1
if (window>len(arr)):
    print("go to hell")

max_sum = float('-inf')
max_window = []


for i in range(len(arr)-1): #6   0,1,2,3,4,5
    
    end = i+window -1
    
    if(len(arr[i:end+1])==window):

        sub_arr = arr[i:end+1]
        w_sum = sum(arr[i:end+1])
        if w_sum > max_sum:
            max_sum = w_sum
            max_arr = sub_arr

print(max_arr)
