import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
Q = 1000000

n = int(input())
p = 15*Q//10  # 나머지 주기
d = [0]*(p+1)
d[1] = 1

for i in range(2,p):
  d[i] = d[i-1]+d[i-2]
  d[i] %= Q

print(d[n%p])