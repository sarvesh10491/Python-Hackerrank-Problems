# https://www.hackerrank.com/challenges/easy-sum/problem

# Test cases
# https://hr-testcases-us-east-1.s3.amazonaws.com/2523/input02.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1527763993&Signature=6rb46GVt79GP3BLPAK3r%2BqM0DIs%3D&response-content-type=text%2Fplain
# https://hr-testcases-us-east-1.s3.amazonaws.com/2523/input05.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1527763472&Signature=IuheOcK34PckXJmrxUP5LT%2FKaZw%3D&response-content-type=text%2Fplain

# Note : Aim is to solve it in minimum possible time for above large dataset test case

def find_sum(N,m):
	numsum=0
	numsetsum=0

	# Break N into sets each containing m numbers & find sum of all numbers in set
	# This set sum will be repeated for all set that fit within N
	numset=N//m
	numsetsum=(m*(m-1))//2
	numsum=numsetsum*numset

	# Find the remaining numbers at the end of list that are not in set & calculate their sum as well
	# Thus we have avoided the time consuming mod operation to get result fast
	temp_m=N-(m*numset)
	numsum=numsum+((temp_m*(temp_m+1))//2)
	print(numsum)


# Input & read from test case dataset
n = int(input())

for i in range(n):
	Nm = input().split()
	N = int(Nm[0])
	m = int(Nm[1])
	find_sum(N,m)