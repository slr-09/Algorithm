import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, v, visited):
  queue = deque([v])
  global count
  visited[v] = True
  while queue:
    x=queue.popleft()
    for i in graph[x]:
      if not visited[i]:
        count += 1
        queue.append(i)
        visited[i] = True
      
n=int(input())
m=int(input())
count=0
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
for i in range(n+1):
  graph[i].sort()
bfs(graph,1,visited)

print(count)