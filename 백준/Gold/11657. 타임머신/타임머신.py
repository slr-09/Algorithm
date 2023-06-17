import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph=[]
dist = [INF]*(n+1)
for _ in range(m):
  a,b,c = map(int,input().split())
  graph.append((a,b,c))

# 벨만 포드 함수
def bf(start):
  # 시작 노드 초기화 
  dist[start] = 0
  # 전체 n번의 라운드 반복
  for i in range(n):
    # 매 라운드마다 모든 간선을 확인 
    for j in range(m):
      cur,next,cost = graph[j][0],graph[j][1],graph[j][2]
      # 현재 간선을 거쳐서 다음 노드로 가는 거리가 더 짧은 경우 
      if dist[cur] != INF and dist[next] > dist[cur]+cost:
        dist[next] = dist[cur]+cost
        # n번째 라운드에서도 값이 갱신된다면 음수 사이클이 존재 
        if i==n-1:
          return True
  return False

cycle = bf(1)

if cycle:
  print("-1")
else:
  for i in range(2,n+1):
    if dist[i] == INF:
      print("-1")
    else:
      print(dist[i])