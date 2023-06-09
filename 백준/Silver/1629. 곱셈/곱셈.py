import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def f(x,n):
  if n==1:
    return x%c
  t = f(x,n//2)
  if n%2==0:
    return (t*t)%c
  else:
    return (t*t*x)%c

print(f(a,b))