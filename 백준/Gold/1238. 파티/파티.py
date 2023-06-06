import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  dist = [INF]*(n+1)
  heapq.heappush(q,(0,start))
  dist[start] = 0
  while q:
    distance,now = heapq.heappop(q)
    if distance > dist[now]:
      continue
    for i in graph[now]:
      cost = distance+i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  return dist
answer = [0 for _ in range(n+1)]
d = dijkstra(x)
for i in range(1,n+1):
  answer[i] += d[i]

for i in range(1,n+1):
  if i==x:
    continue
  d = dijkstra(i)
  answer[i] += d[x]

print(max(answer))
