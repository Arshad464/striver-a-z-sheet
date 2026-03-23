# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#
# *****
#
# *****
#
# *****
#
# *****
#
# *****

def solidsquare(n):
    for i in range(n):
        print("*"*n)

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *
#
# **
#
# ***
#
# ****
#
# *****

def rightTriangleStar(n):
    for i in range(1,n+1):
        print("*"*i)

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#
# 1
#
# 12
#
# 123
#
# 1234
#
# 12345

def rightTriangleColumn(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1
#
# 22
#
# 333
#
# 4444
#
# 55555

def rightTriangleRow(n):
    for i in range(1,n+1):

        print(str(i)*i)

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *****
#
# ****
#
# ***
#
# **
#
# *

def invertedRightTriangle(n):
    for i in range(n,0,-1):
        print("*"*i)

n=int(input())
solidsquare(n)
rightTriangleStar(n)
rightTriangleColumn(n)
rightTriangleRow(n)
invertedRightTriangle(n)