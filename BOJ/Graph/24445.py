import sys
from collections import deque
input = sys.stdin.readline
count=1

def bfs(graph, v, visited):
  queue=deque([v])
  visited[v] = True
  global count
  while queue:
    x=queue.popleft()
    turn[x] = count
    count += 1
    for i in graph[x]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n,m,r = map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
turn = [0 for i in range(n+1)]
for i in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(n):
  graph[i+1].sort(reverse=True)

bfs(graph, r, visited)

for i in range(n):
  print(turn[i+1])
