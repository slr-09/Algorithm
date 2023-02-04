import sys
from collections import deque
input = sys.stdin.readline

def rightcount(num):
  deq = n_deque.copy()
  count1=0
  while(1):
    deq.rotate(1)
    count1 += 1
    if deq[0]==num:  
      break
  return count1

def leftcount(num):
  deq = n_deque.copy()
  count2=0
  while(1):
    deq.rotate(-1)
    count2 += 1
    if deq[0]==num:  
      break
  return count2
  
n = list(map(int,input().split()))
loc = list(map(int,input().split()))
n_deque = deque()

for i in range(n[0]):
  n_deque.append(i+1)

count = 0
for i in range(n[1]):
  if n_deque[0]==loc[i]:  
    n_deque.popleft()
    continue

  num1 = rightcount(loc[i])
  num2 = leftcount(loc[i])
  
  if num1>num2:
    count += num2
    n_deque.rotate(num2*(-1))
    n_deque.popleft()
  else:
    count += num1
    n_deque.rotate(num1)
    n_deque.popleft()
    
print(count)