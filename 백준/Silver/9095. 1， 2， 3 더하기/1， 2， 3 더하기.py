import sys
input = sys.stdin.readline

def f(x):
  if d[x] != 0:
    return d[x]
  if x==1 or x==2:
    d[x] = x
  elif x==3:
    d[x] = 4
  else:
    d[x] = f(x-1)+f(x-2)+f(x-3)
  return d[x]

t = int(input())
d = [0 for _ in range(12)]
for _ in range(t):
  n = int(input())
  print(f(n))

