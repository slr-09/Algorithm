import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
  visited[v] = True
  print(v,end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    x = queue.popleft()
    print(x, end=" ")
    for i in graph[x]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n,m,v = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited1=[False]*(n+1)
visited2=[False]*(n+1)

for i in range(m):
  u,r = map(int,input().split())
  graph[u].append(r)
  graph[r].append(u)

for i in range(n+1):
  graph[i].sort()

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
  