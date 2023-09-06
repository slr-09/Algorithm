import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
for i in range(1,n):
  num[i] += num[i-1]

m = int(input())
for _ in range(m):
  i,j = map(int,input().split())
  if i==1:
    print(num[j-1])
  else:
    print(num[j-1]-num[i-2])