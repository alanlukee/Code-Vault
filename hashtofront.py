str = input()
strlen = len(str)
new_str = ""
for i in str:
    if i =='#':
        new_str = new_str+i
for i in str:
    if i !='#':
        new_str = new_str+i
print(new_str)

    
