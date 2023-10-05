import sys
input = sys.stdin.readline

a = int(input())
b = input().rstrip()
c = int(input())

if b=='+':
  print(a+c)
elif b=='*':
  print(a*c)