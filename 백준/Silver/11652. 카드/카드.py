import sys
input = sys.stdin.readline

n = int(input())
num = dict()
for _ in range(n):
  a = int(input())
  if a in num:
    num[a] += 1
  else:
    num[a] = 1
num = sorted(num.items(), key=lambda x:(-x[1],x[0]))
print(num[0][0])