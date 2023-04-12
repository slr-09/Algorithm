import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = [i+1 for i in range(n)]
for i in range(m):
  a,b = map(int,input().split())
  num[a-1:b] = reversed(num[a-1:b])
  
for i in num:
  print(i,end=" ")