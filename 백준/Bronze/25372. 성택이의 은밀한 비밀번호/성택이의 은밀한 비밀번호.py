import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  str = input().rstrip()
  if len(str) >= 6 and len(str) <= 9:
    print("yes")
  else:
    print("no")