import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
graph=[]
maxNum=0
for _ in range(n):
  num=list(map(int,input().split()))
  graph.append(num)
  for i in num:
    maxNum = max(maxNum,i)
  

dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(x,y,m): 
  q = deque()
  q.append((x,y))
  visited[x][y] = True
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if graph[nx][ny]<m:
        continue
      if visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append((nx,ny))

answer=0
for m in range(maxNum+1):
  count=0
  visited=[[False for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j]==False and graph[i][j]>=m:
        bfs(i,j,m)
        count+=1
  if answer < count:
    answer = count

print(answer)