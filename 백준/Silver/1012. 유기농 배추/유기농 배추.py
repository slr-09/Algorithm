import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if graph[x][y]==1:
    graph[x][y]=0
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

T=int(input())
for i in range(T):
  m,n,k = map(int,input().split())
  
  graph=[[0]*m for _ in range(n)]
  for j in range(k):
    x,y=map(int,input().split())
    graph[y][x] = 1

  result=0
  for j in range(n):
    for h in range(m):
      if dfs(j,h)==True:
        result += 1

  print(result)