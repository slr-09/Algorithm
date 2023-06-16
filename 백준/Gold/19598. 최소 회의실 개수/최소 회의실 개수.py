import sys
import heapq
input = sys.stdin.readline

n=int(input())
li = []
for _ in range(n):
  li.append(list(map(int,input().split())))

li.sort()
count = [li[0][1]]

for i in range(1,len(li)):
  if li[i][0] >= count[0]:
    heapq.heappop(count)
  heapq.heappush(count,li[i][1])

print(len(count))