# https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math
import os
import random
import re
import sys

subs=[]

def remove_dup_list(s):
	i=1
	s.sort()
	dup_s=[]
	dup_s.append(s[0])

	for e in s[1:]:
		if s[i]!=s[i-1]:
			dup_s.append(e)
		i=i+1
	return dup_s

# nonDivisibleSubset function
def nonDivisibleSubset(k, S):
	rem=[]
	for num in S:
		rem.append(num%k)	# Find the remainder for each number%k
	
	remcnt = [0]*k
	for n in rem:
	    remcnt[n] += 1		# Histogram of remainders

	subn = min(remcnt[0], 1)	# Only one number can be in subset as sum of 2 evenly divisible no. by k will also be evenly divisible by k

	for i in range(1,(k//2)+1):
	    if i != k-i:
	        subn += max(remcnt[i], remcnt[k-i])
	    else:
	        subn += min(remcnt[i], 1)

	return subn



if __name__ == '__main__':
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	S = list(map(int, input().rstrip().split()))
	result = nonDivisibleSubset(k, S)
	print(result)
