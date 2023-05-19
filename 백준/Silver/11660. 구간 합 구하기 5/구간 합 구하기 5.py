import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_list=[]
d=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
  n_list.append(list(map(int,input().split())))

for i in range(1,n+1):
  for j in range(1,n+1):
    d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + n_list[i-1][j-1]

for i in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  print(d[x2][y2]-d[x2][y1-1]-d[x1-1][y2]+d[x1-1][y1-1])
      