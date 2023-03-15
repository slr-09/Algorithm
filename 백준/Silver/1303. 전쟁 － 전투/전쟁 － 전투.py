import sys
input = sys.stdin.readline

def dfs(x,y,c):
  if x<0 or x>=m or y<0 or y>=n:
    return False
  if graph[x][y]==c:
    graph[x][y] = 'o'
    global count
    count += 1
    dfs(x-1,y,c)
    dfs(x,y-1,c)
    dfs(x+1,y,c)
    dfs(x,y+1,c)
    return True
  return False
  
n,m = map(int,input().split())
graph=[]
for i in range(m):
  graph.append(list(input().rstrip()))

white=0
blue=0
for i in range(m):
  for j in range(n):
    count = 0
    if dfs(i,j,'W')==True:
      white += count*count
    elif dfs(i,j,'B')==True:
      blue += count*count
print(white,blue)