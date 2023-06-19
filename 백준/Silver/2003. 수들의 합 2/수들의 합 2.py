import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))

start,end = 0,1

answer = 0
while end<=n and start<=end:

  nsum = sum(num[start:end])
  if nsum == m:
    answer += 1
    end += 1
  elif nsum > m:
    start += 1
  else:
    end += 1
print(answer)