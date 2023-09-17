input2 = [4, 9, 5, 3, 2, 10]
output_arr = []

for i in range(len(input2)):
    count = 0
    for j in range(i):
        if input2[j]>input2[i]:
            count = count + 1
    output_arr.append(count)
print(output_arr)

