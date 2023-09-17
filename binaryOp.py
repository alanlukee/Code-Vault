str = '1C1B0A1'

i = 1   
res = int(str[0])  

while i < len(str):       
    operation = str[i]       
    oper2 = int(str[i+1])       
    if operation == 'A':           
        res = res & oper2       
    elif operation == 'B':           
        res = res | oper2       
    else:           
        res = res ^ oper2       
    i += 2   
print(res)

