import math
import os
import random
import re
import sys

cells=[]

def NE(n,r,c):
	if r>=c:
		j=c+1
		for i in range(r+1,n+1):
			if j>n:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i+=1
			j+=1
			

	else:
		i=r+1
		for j in range(c+1,n+1):
			if i>n:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i+=1
			j+=1


def NW(n,r,c):
	if r>=c:
		j=c-1
		for i in range(r+1,n+1):
			if j<1:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i+=1
			j-=1
			

	else:
		i=r+1
		for j in range(c-1,0,-1):
			if i>n:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i+=1
			j-=1
			

def SW(n,r,c):
	if r<=c:
		j=c-1
		for i in range(r-1,0,-1):
			if j<1:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i-=1
			j-=1
			

	else:
		i=r-1
		for j in range(c-1,0,-1):
			if i<1:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i-=1
			j-=1
			

def SE(n,r,c):
	if r<=c:
		j=c+1
		for i in range(r-1,0,-1):
			if j>n:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i-=1
			j+=1
			

	else:
		i=r-1
		for j in range(c+1,n+1):
			if i<1:
				break
			if (i,j) in obstacles:
				break
			cells.append((i,j))
			i-=1
			j+=1
			

def vert(n,r,c):
	j=c
	for i in range(r+1,n+1):
		if (i,j) in obstacles:
				break
		cells.append((i,j))

	for i in range(r-1,0,-1):
		if (i,j) in obstacles:
				break
		cells.append((i,j))

def hori(n,r,c):
	i=r
	for j in range(c+1,n+1):
		if (i,j) in obstacles:
				break
		cells.append((i,j))

	for j in range(c-1,0,-1):
		if (i,j) in obstacles:
				break
		cells.append((i,j))

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
	#print(n, k, r_q, c_q, obstacles)
	NE(n,r_q,c_q)
	NW(n,r_q,c_q)
	SW(n,r_q,c_q)
	SE(n,r_q,c_q)
	vert(n,r_q,c_q)
	hori(n,r_q,c_q)

	# print(tuple(obstacles))
	# print(len(cells))
	return (len(cells))




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