import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,v,visited):
  queue=deque([v])
  visited[v] = True
  while queue:
    x=queue.popleft()
    
    for i in graph[x]:
      if not visited[i]:
        answer[i]=x
        queue.append(i)
        visited[i] = True

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(n-1):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
answer=[0 for _ in range(n+1)]
bfs(graph,1,visited)
for i in range(2,n+1):
  print(answer[i])
