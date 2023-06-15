import sys
input = sys.stdin.readline

r,c = map(int,input().split())
graph = []
check=set()
for _ in range(r):
  graph.append(list(input().rstrip()))

dx,dy = [-1,1,0,0],[0,0,-1,1]
answer = 1

def bfs(x,y):
  q = set()
  q.add((x,y,graph[x][y]))
  global answer
  while q:
    x,y,d = q.pop()
    for i in range(4):
      nx,ny = x+dx[i],y+dy[i]
      if nx<0 or nx>=r or ny<0 or ny>=c or graph[nx][ny] in d:
        continue
      q.add((nx,ny,d+graph[nx][ny]))
      answer = max(answer,len(d)+1)

bfs(0,0)
print(answer)