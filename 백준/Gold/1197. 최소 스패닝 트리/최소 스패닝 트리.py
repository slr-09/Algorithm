import sys
input = sys.stdin.readline

v,e = map(int,input().split())
parent = [i for i in range(v+1)]
graph=[]
result = 0

for _ in range(e):
  a,b,c = map(int,input().split())
  graph.append((c,a,b))

# 비용 순으로 정렬
graph.sort()

# 특정 원소가 속한 집합을 찾을 때까지 
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

# 두 노드가 속한 집합 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

for i in graph:
  cost,a,b = i
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost

print(result)