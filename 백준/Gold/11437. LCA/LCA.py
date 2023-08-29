import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())
d = [0]*(n+1)
c = [False]*(n+1)
parent = [0]*(n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(x,depth):
  c[x] = True
  d[x] = depth
  for i in graph[x]:
    if c[i]:
      continue
    parent[i] = x
    dfs(i,depth+1)

# 최소 공통 조상
def lca(a,b):
  while d[a] != d[b]:
    if d[a] > d[b]:
      a = parent[a]
    else:
      b = parent[b]
  while a != b:
    a = parent[a]
    b = parent[b]
  return a

dfs(1,0)

m = int(input())
for _ in range(m):
  a,b = map(int,input().split())
  print(lca(a,b))