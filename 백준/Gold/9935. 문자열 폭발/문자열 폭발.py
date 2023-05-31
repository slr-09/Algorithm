import sys
input = sys.stdin.readline

str = input().rstrip()
st = input().rstrip()
stack=[]
for i in range(len(str)):
  stack.append(str[i])
  if ''.join(stack[-len(st):]) == st:
    for _ in range(len(st)):
      stack.pop()
      
if stack:
  print(''.join(stack))
else:
  print("FRULA")