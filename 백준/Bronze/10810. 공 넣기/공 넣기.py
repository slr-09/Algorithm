import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num=[0 for _ in range(n)]
for p in range(m):
  i,j,k = map(int,input().split())
  for q in range(i-1,j):
    num[q]=k
for i in num:
  print(i,end=" ")