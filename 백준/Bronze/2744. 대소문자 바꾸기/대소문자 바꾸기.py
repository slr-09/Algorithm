import sys
input = sys.stdin.readline

n = input().rstrip()
for i in n:
  if i.isupper():
    print(i.lower(), end='')
  else:
    print(i.upper(), end='')