# https://www.hackerrank.com/challenges/queens-attack-2/problem

import math
import os
import random
import re
import sys

########################################################################################################
# Below Commented code is implementation of Flood-fill algorithm & can be used to get all cell values
# To only just find no. of cells quickly, use other code
########################################################################################################
# cells=[]

# def NE(n,r,c):
# 	if r>=c:
# 		j=c+1
# 		for i in range(r+1,n+1):
# 			if j>n:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i+=1
# 			j+=1
			

# 	else:
# 		i=r+1
# 		for j in range(c+1,n+1):
# 			if i>n:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i+=1
# 			j+=1


# def NW(n,r,c):
# 	if r>=c:
# 		j=c-1
# 		for i in range(r+1,n+1):
# 			if j<1:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i+=1
# 			j-=1
			

# 	else:
# 		i=r+1
# 		for j in range(c-1,0,-1):
# 			if i>n:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i+=1
# 			j-=1
			

# def SW(n,r,c):
# 	if r<=c:
# 		j=c-1
# 		for i in range(r-1,0,-1):
# 			if j<1:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i-=1
# 			j-=1
			

# 	else:
# 		i=r-1
# 		for j in range(c-1,0,-1):
# 			if i<1:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i-=1
# 			j-=1
			

# def SE(n,r,c):
# 	if r<=c:
# 		j=c+1
# 		for i in range(r-1,0,-1):
# 			if j>n:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i-=1
# 			j+=1
			

# 	else:
# 		i=r-1
# 		for j in range(c+1,n+1):
# 			if i<1:
# 				break
# 			if (i,j) in obstacles:
# 				break
# 			cells.append((i,j))
# 			i-=1
# 			j+=1
			

# def vert(n,r,c):
# 	j=c
# 	for i in range(r+1,n+1):
# 		if (i,j) in obstacles:
# 				break
# 		cells.append((i,j))

# 	for i in range(r-1,0,-1):
# 		if (i,j) in obstacles:
# 				break
# 		cells.append((i,j))

# def hori(n,r,c):
# 	i=r
# 	for j in range(c+1,n+1):
# 		if (i,j) in obstacles:
# 				break
# 		cells.append((i,j))

# 	for j in range(c-1,0,-1):
# 		if (i,j) in obstacles:
# 				break
# 		cells.append((i,j))

# def queensAttack(n, k, r_q, c_q, obstacles):
	# print(n, k, r_q, c_q, obstacles)
	# NE(n,r_q,c_q)
	# NW(n,r_q,c_q)
	# SW(n,r_q,c_q)
	# SE(n,r_q,c_q)
	# vert(n,r_q,c_q)
	# hori(n,r_q,c_q)

########################################################################################################


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
	# List for mininum direction = [ N, NE, E, SE, S, SW, W, NW ]
	mindir=[(n-r_q), min(n-c_q,n-r_q), (n-c_q), min(n-c_q,r_q-1), (r_q-1), min(r_q-1,c_q-1), (c_q-1), min(n-r_q,c_q-1)]
	
	obstdiff=[]
	obst=tuple(obstacles)
	# Find the differnece between obstacle co-ordinates & queen's co-ordinates
	for i,j in obst:
		obstdiff.append((i-r_q, j-c_q))

	# For each obstacle, check its relative position w.r.t. queen's position
	# For every one of 8 directions, calculate no. of cells between them & find lowest cells possible in each direction
	for obr,obc in tuple(obstdiff):
		if obr==0:
			# print("Obstacle in same row as queen")
			if obc<0 and abs(obc)<mindir[6]:	# W
				mindir[6]=abs(obc)-1
			elif obc>0 and abs(obc)<mindir[2]:	# E
				mindir[2]=abs(obc)-1

		elif obc==0:
			# print("Obstacle in same column as queen")
			if obr<0 and abs(obr)<mindir[4]:	# S
				mindir[4]=abs(obr)-1
			elif obr>0 and abs(obr)<mindir[0]:	# N
				mindir[0]=abs(obr)-1

		elif abs(obr)==abs(obc):
			# print("Obstacle in same diagonal as queen")
			if obr>0 and obc>0 and abs(obr)<mindir[1]:		# NE
				mindir[1]=abs(obr)-1
			elif obr>0 and obc<0 and abs(obr)<mindir[7]: 	# NW
				mindir[7]=abs(obr)-1
			elif obr<0 and obc<0 and abs(obr)<mindir[5]: 	# SW
				mindir[5]=abs(obr)-1
			elif obr<0 and obc>0 and abs(obr)<mindir[3]: 	# SE
				mindir[3]=abs(obr)-1

		# else:
			# print("Obstacle has no effect")

		# print(mindir)
	return (sum(mindir))


# Input
if __name__ == '__main__':
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	r_qC_q = input().split()
	r_q = int(r_qC_q[0])
	c_q = int(r_qC_q[1])
	obstacles = []
	
	for _ in range(k):
		obstacles.append(tuple(map(int, input().rstrip().split())))

	result = queensAttack(n, k, r_q, c_q, obstacles)
	print(str(result) + '\n')