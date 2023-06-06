import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start):
  q=[]
  dist = [INF]*(n+1)
  heapq.heappush(q,(0,start))
  dist[start] = 0

  while q:
    di,now = heapq.heappop(q)
    if di > dist[now]:
      continue
    for i in graph[now]:
      cost = di+i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  return dist

answer1=0
answer2=0
d1 = dijkstra(1)
answer1+=d1[v1] 
answer2+=d1[v2]
d2 = dijkstra(v1)
answer1+=d2[v2]
answer2+=d2[n]
d3 = dijkstra(v2)
answer2+=d3[v1]
answer1+=d3[n]

if answer1>=INF or answer2>=INF:
  print("-1")
else:
  print(min(answer1,answer2))
