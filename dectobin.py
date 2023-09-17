print("Decimal to Binary")
decimal = int(input())
binary = ""
while(decimal>0):
    rem = decimal % 2
    binary = binary + str(rem)
    decimal = decimal //2
print(binary)