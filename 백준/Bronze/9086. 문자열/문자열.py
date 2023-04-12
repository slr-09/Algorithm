import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  s=input().rstrip()
  print(s[0],end="")
  print(s[len(s)-1])