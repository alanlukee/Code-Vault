# n = 5
# for row in range(1,n+1,1):
#     for col in range(1,row+1,1):     # INCREASING TRIANGLE
#         print("*",end = "")
#     print(" ")
        
# n = 5
# for row in range(1,n+1,1):
#     for col in range(n):             #box
#         print("*",end ="")
#     print(" ")

# n = 5
# for row in range(1,n+1,1):
#     cols = n-row+1                  #DECREASING TRIANGLE
#     for col in range(cols):
#         print("*",end=" ")
#     print(" ")


# n = 5
# for row in range(1,n+1,1):
#     for col in range(1,row+1,1):     # INCREASING TRIANGLE
#         print(col,end = " ")
#     print(" ")

# n = 5
# for row in range(1,n+1,1):
#     for col in range(1,row+1,1):     
#         print("*",end = " ")
#     print(" ")
# for row in range(2,n+1,1):
#     cols = n-row+1                  #HALF DIAMOND
#     for col in range(cols):
#         print("*",end=" ")
#     print(" ")

# n = 5
# for row in range(1,n+1,1):
#     cols = row
#     for cols in range(cols):
#         print("*",end=" ")
#     print()
# for row in range(2,n+1,1):
#     cols = n-row +1
#     for col in range(cols):
#         print("*",end=" ")
#     print()

#         *  
#       * *
#     * * *
#   * * * *
# * * * * * 

# n=5
# for row in range(1,n+1,1):
#     space = n-row
#     star = row
#     for i in range(space):
#         print(" ",end=" ")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ")


# n = 5
# for row in range(1,n+1,1):
#     spaces = n-row
#     star = row
#     for i in range(spaces):             
#         print(" ",end=" ")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ")

# * * * * *  
#   * * * *
#     * * *
#       * *
#         *

# n = 5
# for row in range(1,n+1,1):
#     space = row - 1
#     star = n - row +1
#     for i in range(space):
#         print(" ",end=" ")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ")

#     *  
#    * *
#   * * *
#  * * * *
# * * * * *

n = 5
for row in range(1,n+1,1):
    star = row
    space = n - row
    for i in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end=" ")
    print(" ")

#       *  
#      * *
#     *   *
#    *     *
#   *       *
#  *         *
# * * * * * * *

# n = 7
# print(" ")
# for row in range(1,n+1,1):
#     if row<=2 or row==n:
#         star = row
#         space = n - row
#         for i in range(space):
#             print(" ",end="")
#         for j in range(star):
#             print("*",end=" ")
#         print(" ")
#     else:
#         space1 = row-2
#         space2 = n - row
#         for j in range(space2):
#             print(" ",end="")
#         print("*",end=" ")
#         for i in range(space1):
#             print(" ",end=" ")
#         print("*")
# print(" ")

#DIAMOND

# n= 3
# for row in range(1,n+1,1):
#     star = row
#     space = n - row
#     for i in range(space):
#         print(" ",end="")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ")
# for row in range(2,n+1,1):
#     space = row -1
#     star = n - row +1
#     for i in range(space):
#         print(" ",end="")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ")

#rhombus

# n = 5
# for row in range(1,n+1,1):
#     space = row - 1
#     star = n-1
#     for i in range(space):
#         print(" ",end="")
#     for i in range(star):
#         print("*",end=" ")
#     print(" ")

#       *  
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *   
# n = 4
# for row in range(1,n+1,1):
#     spaces = n-row
#     star = row
#     for i in range(spaces):             
#         print(" ",end=" ")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ")
# for row in range(2,n+1,1):
#     space = row - 1
#     star = n - row +1
#     for i in range(space):
#         print(" ",end=" ")
#     for j in range(star):
#         print("*",end=" ")
#     print(" ") 

# ****** 
# *    *
# *    *
# ******

# n = 4
# for row in range(1,n+1):
#     if row ==1 or row==4:
#         star = n+2
#         for i in range(star):
#             print("*",end="")
#         print(" ")
#     else: 
#         print("*",end="")
#         for i in range(n):
#             print(" ",end="")
#         print("*",end="")
        
#         print(" ")


# 1
# 3*2
# 4*5*6
# 10*9*8*7

# n = 4
# count = 0
# triangle=[]
# for row in range(1,n+1,1):
#     rows = []
#     for col in range(1,row+1,1):
#         count = count +1
#         rows.append(count)
#     triangle.append(rows)

# for i in range(len(triangle)):
#     if (i+1) % 2 == 0:
#         triangle[i] = triangle[i][::-1]
#     else:
#         triangle[i] = triangle[i]

# for row in triangle:
#     print("*".join(map(str, row)))



# 1
# 23
# 456
# 78910

# 10987
# 654
# 32
# 1
# n = 4
# count = (n*(n+1))//2
# triangle=[]
# for row in range(1,n+1,1):
#     rows = []
#     cols = n-row +1
#     for col in range(cols):
#         rows.append(count)
#         count = count -1
#     triangle.append(rows)

# for row in triangle:
#     print("".join(map(str, row)))





    


