import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[]

for i in range(n):
  nn = list(map(int,input().split()))
  for j in range(len(nn)):
    if nn[j]==2:
      start = (i,j)
    elif nn[j]==1:
      nn[j] = -1
  graph.append(nn)
  
graph[start[0]][start[1]] = 0
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == -1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]
  
bfs(start[0],start[1])

for i in range(len(graph)):
  for j in range(len(graph[0])):
    print(graph[i][j],end=" ")
  print()