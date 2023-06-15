import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

visited = [False]*(n+1)
dist = [0]*(n+1)
def dfs(x):
  visited[x] = True
  for i in graph[x]:
    if not visited[i[0]]:
      dist[i[0]] = dist[x]+i[1]
      dfs(i[0])

dfs(1)
m = dist.index(max(dist))
visited = [False]*(n+1)
dist = [0]*(n+1)
dfs(m)
print(max(dist))