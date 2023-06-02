import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
array = [0]*100001

def bfs(v):
  queue = deque([v])
  while queue:
    v = queue.popleft()
    if v==k:
      return array[v]
    for i in (v-1,v+1,v*2):
      if 0<=i<100001 and not array[i]:
        array[i] = array[v]+1
        queue.append(i)

print(bfs(n))