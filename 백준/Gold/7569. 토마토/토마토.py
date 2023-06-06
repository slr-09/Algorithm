import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph=[[] for _ in range(h)]
dx,dy,dz=[-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]
queue = deque()

for r in range(h):
  for i in range(n):
    to = list(map(int,input().split()))
    graph[r].append(to)
    for j in range(len(to)):
      if to[j]==1:
        queue.append((i,j,r))

def bfs():
  while queue:
    x,y,z = queue.popleft()
    for i in range(6):
      nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
      if nx<0 or nx>=n or ny<0 or ny>=m or nz<0 or nz>=h:
        continue
      if graph[nz][nx][ny] == -1 or graph[nz][nx][ny]>0:
        continue
      if graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y]+1
        queue.append((nx,ny,nz))

bfs()
answer=0
for i in range(h):
  c=False
  for j in range(n):
    if 0 in graph[i][j]:
      c=True
      break
    answer = max(answer, max(graph[i][j]))
  if c:  
    answer=0
    break
  
print(answer-1)