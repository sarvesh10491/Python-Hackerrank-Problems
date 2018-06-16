# https://www.hackerrank.com/challenges/3d-surface-area/problem

import math
import os
import random
import re
import sys


# Complete the surfaceArea function below.
def surfaceArea(A):
	SA=0
	for i in range(len(A)):
		for j in range(len(A[i])):
			if A[i][j]!=0:					# To check if 1x1 block exist or not
				SA+=2						# For any position, it will always have 1 unit area top & 1 unit area bottom surface

				# Surface area formed wrt to blocks on right side of grid
				if j==len(A[i])-1:			# Check for corner case
					SA+=A[i][j]
				elif A[i][j]>A[i][j+1]:
					SA+=A[i][j]-A[i][j+1]

				# Surface area formed wrt to blocks on left side of grid
				if j==0:					# Check for corner case
					SA+=A[i][j]
				elif A[i][j]>A[i][j-1]:
					SA+=A[i][j]-A[i][j-1]

				# Surface area formed wrt to blocks on above of grid
				if i==0:					# Check for corner case
					SA+=A[i][j]
				elif A[i][j]>A[i-1][j]:
					SA+=A[i][j]-A[i-1][j]

				# Surface area formed wrt to blocks on below of grid
				if i==len(A)-1:				# Check for corner case
					SA+=A[i][j]
				elif A[i][j]>A[i+1][j]:
					SA+=A[i][j]-A[i+1][j]
	return SA
	

if __name__ == '__main__':
	HW = input().split()
	H = int(HW[0])
	W = int(HW[1])
	A = []

	for _ in range(H):
		A.append(list(map(int, input().rstrip().split())))

	result = surfaceArea(A)
	print(str(result) + '\n')