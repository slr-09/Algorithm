import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

m,n,k = map(int,input().split())
graph=[[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for i in range(m-y2,m-y1):
    for j in range(x1,x2):
      graph[i][j] = 1

count=0

def dfs(x,y):
  if x<0 or x>=m or y<0 or y>=n:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    global num
    num += 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False
answer=[]
for i in range(m):
  for j in range(n):
    num=0
    if dfs(i,j)==True:
      count += 1
      answer.append(num)
answer.sort()
print(count)
for i in answer:
  print(i,end=" ")