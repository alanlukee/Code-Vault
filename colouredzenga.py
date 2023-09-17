arr = ['red', 'white', 'white', 'red']
moves = 0
i = 0

while(i<len(arr)):
    if arr[i] != arr[i+1]:
        moves = moves+1
print(moves)
