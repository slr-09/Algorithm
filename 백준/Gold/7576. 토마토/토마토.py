import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph=[]
dx,dy=[-1,1,0,0],[0,0,-1,1]
queue = deque()

for i in range(n):
  to = list(map(int,input().split()))
  graph.append(to)
  for j in range(len(to)):
    if to[j]==1:
      queue.append((i,j))

def bfs():
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx,ny = x+dx[i],y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == -1 or graph[nx][ny]>0:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))

bfs()
answer=0
for i in range(n):
  if 0 in graph[i]:
    answer=0
    break
  answer = max(answer, max(graph[i]))

print(answer-1)