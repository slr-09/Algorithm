import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
array = [0]*100001
visited=[False]*100001
def bfs(v):
  queue = deque([v])
  while queue:
    v = queue.popleft()
    if v==k:
      return array[v]
    if 0<=2*v<100001 and not visited[2*v]:
      array[2*v] = array[v]
      queue.append(2*v)
      visited[2*v] = True
    for i in (v-1,v+1):
      if 0<=i<100001 and not visited[i]:
        array[i] = array[v]+1
        queue.append(i)
        visited[i] = True

print(bfs(n))