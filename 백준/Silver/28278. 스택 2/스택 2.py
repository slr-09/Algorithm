import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
  nn = list(map(int,input().split()))
  if nn[0] == 1:
    stack.append(nn[1])
  elif nn[0] == 2:
    if len(stack)==0:
      print(-1)
    else: 
      print(stack.pop())
  elif nn[0] == 3:
    print(len(stack))
  elif nn[0] == 4:
    if len(stack)==0:
      print(1)
    else:
      print(0)
  elif nn[0] == 5:
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])