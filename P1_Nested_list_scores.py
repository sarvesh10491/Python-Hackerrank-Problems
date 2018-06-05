# https://www.hackerrank.com/challenges/nested-list/problem

# n = int(input())

# students = []
 
# for i in range(n):
#     name = input()
#     mark = input()
#     students.append([name, float(mark)])

students = [['Harry', 20], ['Berry', 20], ['Tina', 19], ['Akriti', 19], ['Harsh', 21]]

scores=[]
sec_studs=[]
count=0

# Build the scores only list to find minimum overall score
for i in range(len(students)):
	scores.append(students[i][1])
lowest=min(scores)
#print(lowest)

# Find how many such lowest score exist in list & remove them from original list
for i in range(len(scores)):
	if scores[i]==lowest:
		count=count+1
for i in range(count):
	scores.remove(lowest)


# Minimum of new list will be second minimum of original score list
sec_lowest=min(scores)
#print(sec_lowest)

# Compare this second minimum score with scores in original student list to find all matched students & append to final solution list
for i in range(len(students)):
	if students[i][1]==sec_lowest:
		sec_studs.append(students[i])
sec_studs.sort()

for i in range(len(sec_studs)):
	print(sec_studs[i][0])