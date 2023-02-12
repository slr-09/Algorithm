import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
n_deque=deque()

for i in range(n):
  n_deque.append(i+1)
n_list=[]
while(len(n_deque)):
  n_deque.rotate((k-1)*(-1))
  n_list.append(n_deque.popleft())

print("<"+", ".join(list(map(str,n_list)))+">")
