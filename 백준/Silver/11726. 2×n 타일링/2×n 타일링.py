import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n=int(input())
d=[0]*1001
d[1] = 1
d[2] = 2

def f(x):
  if d[x] != 0:
    return d[x]
  d[x] = f(x-1)+f(x-2)
  return d[x]
  
print(f(n)%10007)