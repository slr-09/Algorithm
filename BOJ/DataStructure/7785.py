import sys
input = sys.stdin.readline

n = int(input())
n_set=set()
for i in range(n):
  name, st = map(str,input().split())
  if st=="leave":
    n_set.remove(name)
  else:  
    n_set.add(name)
  
for i in sorted(n_set,reverse=True):
  print(i)
