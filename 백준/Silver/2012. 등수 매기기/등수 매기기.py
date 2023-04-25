import sys
input = sys.stdin.readline

n=int(input())
score=[]
sc=[i+1 for i in range(n)]
for i in range(n):
  score.append(int(input()))
score.sort()
sum=0
for i in range(n):
  sum += abs(score[i]-sc[i])

print(sum)