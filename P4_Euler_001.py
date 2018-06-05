# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

# Similar to problem 2 aim is to get result in minimum time

n=1000000000

def nsum(k):
    return ((k*(k+1))//2)

def euler001(n):
    esum=0
    num3=(n-1)//3
    num5=(n-1)//5
    num15=(n-1)//15
    esum=(nsum(num3)*3)+(nsum(num5)*5)-(nsum(num15)*15)
    print(esum)

# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     euler001(n)
    
euler001(n)
