import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
num = [1, 1, 2, 2, 2, 8]
for i in range(len(n)):
  n[i] = num[i] - n[i]

for i in range(len(n)):
  print(n[i],end=' ')