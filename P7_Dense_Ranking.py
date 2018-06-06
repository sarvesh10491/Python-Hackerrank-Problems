# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

alice_rank=[]

def climbingLeaderboard(scores, alice):
	for alice_score in alice:
		i=0
		rank=1
		rank_flag=0
		
		while alice_score<scores[i]:
			if i>0:
				if scores[i]==scores[i-1]:
					rank_flag+=1

			i+=1
			if i==len(scores):
				# print("Alice is currently lowest ranked")
				break
		alice_rank.append(rank+i-rank_flag)

	#print(alice_rank)
	for i in range(len(alice_rank)):
		print(alice_rank[i])


# Input reading
if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    climbingLeaderboard(scores, alice)