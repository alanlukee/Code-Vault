arr = "bbabbccbb"
dict = {}
for i in arr:
    if i not in dict.keys():  
        dict[i] = 1    
    else:
        dict[i] = dict[i]+1

max_value = 0
max_key = ''
for key, value in dict.items():
    if value > max_value:
        max_value = value
        max_key = key

x = arr.replace(max_key, 't')
print(x)
