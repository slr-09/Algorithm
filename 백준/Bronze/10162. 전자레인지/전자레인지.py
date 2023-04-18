import sys
input = sys.stdin.readline

t=int(input())
sec = [[300,0],[60,0],[10,0]]

for i in range(3):
  sec[i][1] += t//sec[i][0]
  t %= sec[i][0]

if t==0:
  for i in range(3):
    print(sec[i][1],end=" ")
else:
  print("-1")