import sys
import heapq
input = sys.stdin.readline

n=int(input())
c_time=[]

for i in range(n):
  c_time.append(list(map(int,input().split())))
c_time.sort()
answer=[]
heapq.heappush(answer,c_time[0][1])
for i in range(1,n):
  if answer[0] <= c_time[i][0]:
    heapq.heappop(answer)
  heapq.heappush(answer,c_time[i][1])  
    
print(len(answer))