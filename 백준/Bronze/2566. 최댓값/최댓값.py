import sys
input = sys.stdin.readline

max=0
x,y=0,0
for i in range(9):
  num = list(map(int,input().split()))
  for j in range(9):
    if max <= num[j]:
      max = num[j]
      x,y = i+1,j+1

print(max)
print(x,y)