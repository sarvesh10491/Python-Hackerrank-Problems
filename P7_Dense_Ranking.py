# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

# Remove Duplicate scores to trim list for fast access
def remove_dup_list(s):
	i=1
	dup_s=[]
	dup_s.append(s[0])

	for e in s[1:]:
		if s[i]!=s[i-1]:
			dup_s.append(e)
		i=i+1
	return dup_s


# Binary Search for better time complexity
def binary_search_func(s,e,pos):
	if len(s)>1:
		p=(len(s))//2
		if e==s[p]:
			return (pos+1)
		elif e>s[p]:
			pos=pos-(len(s[:p])-((len(s[:p]))//2))
			return binary_search_func(s[:p],e,pos)
		else:
			pos=pos+((len(s[p:]))//2)
			return binary_search_func(s[p:],e,pos)

	else:
		if e==s[0]:
			return (pos+1)
		elif e<s[0]:
			return (pos+2)


def find_pos(s,e):
	pos=(len(s))//2
	return (binary_search_func(s,e,pos))



def climbingLeaderboard(scores, alice):
	scores_updated=remove_dup_list(scores)

	for alice_score in alice:
		if alice_score>=scores_updated[0]:
			rank=1
		elif alice_score==scores_updated[-1]:
			rank=len(scores_updated)
		elif alice_score<scores_updated[-1]:
			rank=len(scores_updated)+1
		else:
			rank=find_pos(scores_updated,alice_score)
		print(rank)

# Input reading
if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    climbingLeaderboard(scores, alice)