print("Enter String:")
str = input()

x = ""
arr = []
for i in range(len(str)):
    if str[i].isupper():
        arr.append(i)
        
str = str.upper()

x = []
s = ""
for i in range(len(str)):
    if i not in arr:
        s += str[i]
    else:
        if s:
            x.append(s)
            s = ""
        s += str[i].lower()

if s:
    x.append(s)

for i in x:
    print(i)
        
# str = "helloWorldAlanLukeAswinAkashGout"
# for i in str:
#     if i.islower():
#         print(i.upper(), end="")
#     elif i.isupper():
#         print()
#         print(i.lower(), end="")
  