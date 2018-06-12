# https://www.hackerrank.com/challenges/the-grid-search/problem

import math
import os
import random
import re
import sys

# Function to find all possible starting indices of pattern substring in main string
def found_at(parentstr, substr):
	indices=[]
	i = parentstr.find(substr)
	while i >= 0:
		indices.append(i)
		i = parentstr.find(substr, i+1)
	return indices


def gridSearch(G, P):
	gi=0
	pi=0
	# Check grid only till we can ensure pattern can fit to be found & not search entire grid to last line
	while gi<(len(G)-len(P)+1):
		idx=G[gi].find(P[pi])
		if idx!=-1:				# 1st line of pattern found in one of the line
			# Find indices of all matching paterns in line
			# ps = [pat.start() for pat in re.finditer(re.escape(P[pi]), G[gi])]	<= This didnt work as it skips current successful pattern in next search
			ps = found_at(G[gi],P[pi])
			# print("Found in line",gi,"at",ps)
			for k in ps:		# For each index as starting point
				idx=k
				tgi=gi
				tpi=0
				while tpi<len(P):	# Check all subsequent lines in grid to see if respective subsequent lines in pattern also exist in them
					tidx=G[tgi+tpi].find(P[tpi],idx)
					if tidx!=idx:
						break
					else:
						tpi+=1
						if tpi==len(P):
							return ("YES")
			gi+=1
		else:
			gi+=1

	return ("NO")


# Input
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)
