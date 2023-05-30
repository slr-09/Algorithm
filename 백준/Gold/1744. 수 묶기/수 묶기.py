import sys
import heapq
input = sys.stdin.readline

n=int(input())
heap=[]
heap2=[]
c=0
for _ in range(n):
  num = int(input())
  if num>0:
    heapq.heappush(heap,num*(-1))
  elif num==0:
    c += 1
  else:
    heapq.heappush(heap2,num)

sum=0
while True:
  if len(heap)==0:  
    break
  num1 = heapq.heappop(heap)*(-1)
  if len(heap)==0:
    sum += num1
    break
  num2 = heapq.heappop(heap)*(-1)
  if num2==1:
    sum += num1+num2
  else:
    sum += num1*num2
  
while True:
  if len(heap2)==0:
    break
  if len(heap2)==1 and c>0:
    break
  num1 = heapq.heappop(heap2)
  if len(heap2)==0:
    sum += num1
    break
  num2 = heapq.heappop(heap2)
  sum += num1*num2
  
print(sum)
    