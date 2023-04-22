import sys
input = sys.stdin.readline

n=int(input())
d = [0]*117

def fibo(n):
  if n==1 or n==2 or n==3:
    return 1
  if d[n] != 0:
    return d[n]
  d[n] = fibo(n-1) + fibo(n-3)
  return d[n]

print(fibo(n))