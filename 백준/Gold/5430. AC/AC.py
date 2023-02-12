import sys
from collections import deque
input = sys.stdin.readline

T=int(input())

for i in range(T):
  check=True
  check2=True
  str3=input()
  n=int(input())
  if n>0:
    str2 = input().replace("[","").replace("]","")
    n_list = deque(map(int,str2.split(",")))
  else:
    str2 = input()
    n_list=deque()
  for j in range(len(str3)):
    if str3[j]=="R":
      check = not(check)
    elif str3[j]=="D":
      if len(n_list)==0:  
        print("error")
        check2=not(check2)
        break
      else:  
        if check:
          n_list.popleft() 
        else:
          n_list.pop()
  if check2:
    n_list=list(n_list)
    if not(check):
      n_list.reverse()
    print("["+",".join(list(map(str,n_list)))+"]")
