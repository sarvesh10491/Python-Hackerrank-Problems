# https://www.hackerrank.com/challenges/the-minion-game/problem

s = 'BANANA'

List_vow=['A','E','I','O','U']

def minion_game(s):
	count_vow=0
	count_con=0
	tracker=0
	totch=len(s)
	for c in s:
		if c in List_vow:
			count_vow+=(totch-tracker)
		else:
			count_con+=(totch-tracker)
		tracker+=1
	#print(count_vow,count_con)
	if count_vow>count_con:
		print("Kevin",count_vow)
	elif count_vow<count_con:
		print("Stuart",count_con)
	else:
		print("Draw")

minion_game(s)