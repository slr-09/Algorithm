import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
q2 = []
for _ in range(n):
  num = int(input())
  if len(q) == len(q2):
    heapq.heappush(q,-num)
  else:
    heapq.heappush(q2,num)
  if q2 and q2[0] < -q[0]:
    p = heapq.heappop(q)
    p2 = heapq.heappop(q2)

    heapq.heappush(q,-p2)
    heapq.heappush(q2,-p)

  print(-q[0])
