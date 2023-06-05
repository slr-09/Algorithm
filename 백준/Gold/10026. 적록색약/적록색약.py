import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph1=[]
graph2=[[] for _ in range(n)]
for j in range(n):
  st = list(input().rstrip())
  graph1.append(st)
  for x in st:
    if x=='G':
      graph2[j].append('R')
    else:
      graph2[j].append(x)
    
def dfs(x,y,m,graph):
  if x<0 or x>=n or y<0 or y>=n:
    return False
  if graph[x][y] == m:
    graph[x][y]='T'
    dfs(x-1,y,m,graph)
    dfs(x+1,y,m,graph)
    dfs(x,y-1,m,graph)
    dfs(x,y+1,m,graph)
    return True
  return False
answer1,answer2=0,0

for i in range(n):
  for j in range(n):
    for x in ('B','R','G'):
      if dfs(i,j,x,graph1)==True:
        answer1 += 1
      if dfs(i,j,x,graph2)==True:
        answer2 += 1
    
print(answer1,answer2)