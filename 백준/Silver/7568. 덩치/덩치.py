import sys
input = sys.stdin.readline

n=int(input())
n_list = []
people = []
for i in range(n):
  n_list = list(map(int, input().split()))
  people.append(n_list)
rank = []
for i in range(n):
  count=0
  for j in range(n):
    if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
      count+=1
  rank.append(count+1)

for i in rank:
  print(i,end=" ")