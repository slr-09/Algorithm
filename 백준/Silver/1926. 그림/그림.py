import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
  global count
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if graph[x][y]==1:
    count += 1
    graph[x][y]=0
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

n,m = map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

result=0
max=0
num=[]
for i in range(n):
  for j in range(m):
    count=0
    if dfs(i,j)==True:
      if max<count:
        max = count
      result += 1
print(result)
print(max)