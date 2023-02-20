import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
count=1

def dfs(graph, v, visited):
  visited[v] = True
  global count
  turn[v] = count
  count += 1
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

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

dfs(graph, r, visited)

for i in range(n):
  print(turn[i+1])