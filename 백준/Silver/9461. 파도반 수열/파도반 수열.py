import sys
input = sys.stdin.readline

def f(n):
  if n==1 or n==2 or n==3:
    return 1
  if d[n] != 0:
    return d[n]
  d[n] = f(n-3)+f(n-2)
  return d[n]

T = int(input())
for i in range(T):
  n=int(input())
  d=[0]*(n+1)
  print(f(n))