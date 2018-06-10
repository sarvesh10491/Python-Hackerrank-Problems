# https://www.hackerrank.com/challenges/encryption/problem

import math
import os
import random
import re
import sys


# Function to remove spaces
def remove_spaces(s):
	stmp=[]
	for c in s:
		if c!=" ":
			stmp.append(c)
	return stmp

# Encrption function
def encryption(s):
	s=remove_spaces(s)
	L=len(s)
	rows=math.floor(math.sqrt(L))
	cols=math.ceil(math.sqrt(L))

	# Find rows X columns combination for which floor(sqrt(L))<=rows<=columns<=ceil(sqrt(L)) and size is minimum
	r=rows
	pr=[]
	while r<=cols:
		pr.append(r)
		r+=1
		if (rows*cols)>=L:
			break
	rows=max(pr)	

	Mat = [[" "] * cols for i in range(rows)]

	# Update 2-D matrix with input string
	i,j,c=0,0,0
	while i<rows:
		while j<cols:
			if c<L:
				Mat[i][j]=s[c]

			c+=1
			j+=1
		i+=1
		j=0

	# Re-arrange matrix with given encryption rule
	encrypt=[]
	i,j=0,0
	while j<cols:
		while i<rows:
			if Mat[i][j]!=" ":
				encrypt.append(Mat[i][j])
			i+=1
		encrypt.append(" ")
		i=0
		j+=1

	# print(encrypt)
	return ("".join(encrypt))



if __name__ == '__main__':
	s = input()
	result = encryption(s)
	print(result + '\n')