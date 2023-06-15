import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

v=int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
  n = list(map(int,input().split()[:-1]))
  for i in range(1,len(n)-1,2):
    graph[n[0]].append((n[i],n[i+1]))

visited=[False]*(v+1)
dist=[0]*(v+1)

def dfs(x):
  visited[x] = True
  for i in graph[x]:
    if not visited[i[0]]:
      dist[i[0]] = dist[x]+i[1]
      dfs(i[0])

dfs(1)
m = dist.index(max(dist))
visited=[False]*(v+1)
dist=[0]*(v+1)
dfs(m)
print(max(dist))