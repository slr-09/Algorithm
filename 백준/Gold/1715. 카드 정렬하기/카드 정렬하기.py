import sys
import heapq
input = sys.stdin.readline

n=int(input())
card=[]
for i in range(n):
  heapq.heappush(card,int(input()))

sum=0
for i in range(n-1):
  num = heapq.heappop(card)+heapq.heappop(card)
  heapq.heappush(card, num)
  sum += num
  
print(sum)