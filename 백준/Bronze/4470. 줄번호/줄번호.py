import sys
input = sys.stdin.readline


n = int(input())
for i in range(n):
  st = input().rstrip()
  print(str(i+1)+". "+st)