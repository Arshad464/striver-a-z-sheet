# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 12345
#
# 1234
#
# 123
#
# 12
#
# 1

def righttrianglenum(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(j+1,end="")
        print()


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#     *
#    ***
#   *****
#  *******
# *********


def starpyramid(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*((2*i)+1))

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *********
#  *******
#   *****
#    ***
#     *

def invertedStarPyramid(n):
    for i in range(n-1,-1,-1):
        print(" "*(n-i-1)+"*"*(2*i+1))
n=int(input())


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def starDiamond(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))
    for i in range(n):
        print(" "*(i)+"*"*(2*(n-i)-1))

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
#
# ****
#
# ***
#
# **
#
# *

def rightAlignedDiamond(n):
    for i in range(1,n+1):
        print("*"*i)
    for i in range(n-1,0,-1):
        print("*"*i)

righttrianglenum(n)
starpyramid(n)
invertedStarPyramid(n)
starDiamond(n)
rightAlignedDiamond(n)