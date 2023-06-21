import sys
input = sys.stdin.readline

n,m = int(input()), int(input())
graph=[]
parent = [i for i in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph.append((c,a,b))

graph.sort()

def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b
result = 0
for i in graph:
  cost,a,b = i
  if find_parent(parent,a)!=find_parent(parent,b):
    union(parent,a,b)
    result += cost

print(result)