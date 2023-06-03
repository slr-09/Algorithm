import sys
input = sys.stdin.readline

n=int(input())
n_list = list(map(int,input().split()))
d=[1 for _ in range(n)]
for i in range(n):
  for j in range(i):
    if n_list[i] > n_list[j]:
      d[i] = max(d[i],d[j]+1)

print(max(d))