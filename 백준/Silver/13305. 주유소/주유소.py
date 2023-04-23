# 17점
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
-----------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
dist=deque(map(int,input().split()))
cost=list(map(int,input().split()))
cost.pop()
answer=0
for i in range(n-1):
  if cost[i]>min(cost):
    answer += cost[i]*dist.popleft()
  elif cost[i]==min(cost):
    answer += sum(dist)*cost[i]
    break

print(answer)

-----------------------------------------
# 100점
import sys
input = sys.stdin.readline

n=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))
answer=0
mincost=cost[0]
for i in range(n-1):
  mincost = min(mincost,cost[i])
  answer += mincost*dist[i]

print(answer)
