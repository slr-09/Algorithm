import sys
input = sys.stdin.readline
        
def dfs(x,y):
  if x<0 or x>=n or y<0 or y>=n:
    return False
  
  if graph[x][y]==1:
    global count
    count += 1
    graph[x][y]=-1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

n = int(input())
graph=[[] for _ in range(n)]
for i in range(n):
  p = input()
  for j in range(n):
    graph[i].append(int(p[j]))

result=0
count=0
list=[]
for i in range(n):
  for j in range(n):
    count=0
    if dfs(i,j)==True:
      list.append(count)
      result += 1

list.sort()
print(result)
for i in list:
  print(i)