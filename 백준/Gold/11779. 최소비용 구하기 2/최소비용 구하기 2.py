import sys
import heapq
import copy
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

start,end = map(int,input().split())
path=[[] for _ in range(n+1)]

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  path[start].append(start)  
  dist[start] = 0
  while q:
    distance,now = heapq.heappop(q)
    if distance > dist[now]:
      continue
    for i in graph[now]:
      cost = distance + i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        path[i[0]] = copy.deepcopy(path[now])
        path[i[0]].append(i[0])
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(dist[end])
print(len(path[end]))
for i in path[end]:
  print(i,end=' ')