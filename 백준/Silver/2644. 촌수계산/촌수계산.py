import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
distance[a] = 0
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    for i in graph[v]:
        if distance[i] != -1:
            continue
        distance[i] = distance[v]+1
        dfs(i)

dfs(a)
print(distance[b])