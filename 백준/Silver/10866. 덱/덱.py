import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
n_deque = deque()
for i in range(n):
  str = list(input().split())
  if str[0]=="push_front":
    n_deque.appendleft(str[1])
  elif str[0]=="push_back":
    n_deque.append(str[1])
  elif str[0]=="pop_front":
    if len(n_deque)==0:  print("-1")
    else: print(n_deque.popleft())
  elif str[0]=="pop_back":
    if len(n_deque)==0:  print("-1")
    else: print(n_deque.pop())
  elif str[0]=="size":
    print(len(n_deque))
  elif str[0]=="empty":
    if len(n_deque)==0:  print("1")
    else:  print("0")
  elif str[0]=="front":
    if len(n_deque)==0:  print("-1")
    else:  print(n_deque[0])
  elif str[0]=="back":
    if len(n_deque)==0:  print("-1")
    else:  print(n_deque[-1])