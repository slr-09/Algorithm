import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(n,m):
  for i in range(n):
    for j in range(m):
      cur,next,cost = graph[j]
      if dist[next] > dist[cur]+cost:
        dist[next] = dist[cur]+cost
        if i==n-1:
          return True
  return False

t = int(input())
for _ in range(t):
  n,m,w = map(int,input().split())
  graph=[]
  dist = [INF]*(n+1)
  for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))
    graph.append((b,a,c))
  for _ in range(w):
    a,b,c = map(int,input().split())
    graph.append((a,b,-c))
  
  cycle = bf(n,len(graph))

  if cycle:
    print("YES")
  else:
    print("NO")
