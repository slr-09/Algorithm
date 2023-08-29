import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    for k in range(n):
      if graph[j][i] and graph[i][k]:
        graph[j][k] = 1

for i in range(n):
  for j in range(n):
    print(graph[i][j], end=' ')
  print()