import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
d = [-1]*(n+1)
d[x] = 0
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

def bfs(v):
  queue = deque()
  queue.append(v)
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if d[i]==-1:
        d[i] = d[v]+1
        queue.append(i)

bfs(x)

check = False
for i in range(n):
  if d[i+1] == k:
    check = True
    print(i+1)

if not check:
  print(-1)