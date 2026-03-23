# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1
#
# 0 1
#
# 1 0 1
#
# 0 1 0 1
#
# 1 0 1 0 1

def binaryTriangle(n):
    for i in range(1,n+1):
        for j in range(i):
            if (i+j)%2==0:
                print("0",end="")
            else:
                print("1",end="")
        print()


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

def palindromicNumPyramid(n):
    for i in range(1,n+1):
        for j in range(1,2*n+1):
            if j<=i:
                print(j,end="")
            elif j<2*n-i+1:
                print(" ",end="")
            else:
                print(2*n-j+1,end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1
#
# 2 3
#
# 4 5 6
#
# 7 8 9 10
#
# 11 12 13 14 15

def floydTriangle(n):
    num=1
    for i in range(n):
        for j in range(i+1):
            print(num,end=" ")
            num+=1
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# A
#
# AB
#
# ABC
#
# ABCD
#
# ABCDE

def alphabetTriangle(n):
    for i in range(1,n+1):
        c=65
        for j in range(i):
            print(chr(c),end=" ")
            c+=1
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# ABCDE
#
# ABCD
#
# ABC
#
# AB
#
# A

def invertedAlphabetTriangle(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j),end=" ")
        print()

n=int(input())
binaryTriangle(n)
palindromicNumPyramid(n)
floydTriangle(n)
alphabetTriangle(n)
invertedAlphabetTriangle(n)