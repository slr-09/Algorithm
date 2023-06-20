import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
s = int(input())

for i in range(n):
  maxnum = max(num[i:min(n,i+s+1)])
  idx = num.index(maxnum)

  for j in range(idx, i, -1):
    num[j],num[j-1] = num[j-1],num[j]
    
  s -= (idx-i)
  if s<=0:
    break

print(*num)