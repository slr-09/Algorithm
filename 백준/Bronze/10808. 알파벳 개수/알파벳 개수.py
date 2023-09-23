import sys
import string
input = sys.stdin.readline

lower = [i for i in string.ascii_lowercase]
n = [0 for _ in range(len(lower))]
str = input().rstrip()
for i in range(len(str)):
  if str[i] in lower:
    n[lower.index(str[i])] += 1

for i in n:
  print(i, end=" ")