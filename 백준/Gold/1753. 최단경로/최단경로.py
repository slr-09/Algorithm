import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
dist = [INF]*(v+1)
for _ in range(e):
  a,b,c = map(int,input().split())
  # 노드 a에서 b로 가는 가중치가 c
  graph[a].append((b,c))


def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  dist[start] = 0
  while q:
    distance,now = heapq.heappop(q)
    # 이미 처리된 노드라면 무시 
    if dist[now] < distance:
      continue
    for i in graph[now]:
      cost = distance + i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,v+1):
  if dist[i]==INF:
    print("INF")
  else:
    print(dist[i])