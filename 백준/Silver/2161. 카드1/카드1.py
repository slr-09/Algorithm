import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
n_deque = deque()
for i in range(n):
  n_deque.append(i+1)

n_list=[]
while(len(n_deque)):
  n_list.append(n_deque.popleft())
  n_deque.rotate(-1)

for i in n_list:
  print(i, end=" ")