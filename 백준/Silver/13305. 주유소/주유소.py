import sys
input = sys.stdin.readline

n=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))
cost.pop()
answer=0
for i in range(n-1):
  if cost[i]>min(cost):
    answer += cost[i]*dist[i]
  elif cost[i]==min(cost):
    sum=0
    for j in range(i,n-1):
      sum += dist[j]
    answer += sum*cost[i]
    break

print(answer)