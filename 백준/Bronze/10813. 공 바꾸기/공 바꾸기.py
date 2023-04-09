import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num=[i+1 for i in range(n)]
for p in range(m):
  i,j = map(int,input().split())
  temp = num[i-1]
  num[i-1] = num[j-1]
  num[j-1] = temp
for i in num:
  print(i,end=" ")