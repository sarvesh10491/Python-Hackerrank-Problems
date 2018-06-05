# https://www.hackerrank.com/challenges/sherlock-and-divisors/forum

import math

num=16

primes=[]
odd_primes=[]


def list_primes(n):
	root=2
	a=range(n)
	i=2

	while i < n:
		if root > math.sqrt(a[i]):
			primes.append(a[i])
			root=2
			i=i+1
		elif a[i]%root==0:
			root=2
			i=i+1
		else:
			root=root+1

def find_factors(primes):
	cnt=0
	numfact=1
	pripow=[]
	for i in primes:
		t_num=num
		pripow.append(0)
		while t_num%i==0:
			t_num=t_num//i
			pripow[cnt]+=1
		cnt+=1

	#print("Prime powers :",pripow)

	for i in pripow:
		if i!=0:
			numfact*=(i+1)
	

	return numfact

list_primes(num//2)
#print("All primes :",primes)

if primes[0]==2:
	odd_primes=primes[1:]
else:
	odd_primes=primes

fact_total=find_factors(primes)
fact_odd=find_factors(odd_primes)
fact_even=fact_total-fact_odd

print("Total factors :",fact_total)
print("Odd factors :",fact_odd)
print("Even factors :",fact_even)