import sys
input = sys.stdin.readline

s=input()
for i in range(len(s)):
  print(s[i],end="")
  if i%10==9 and i!=len(s)-1:  print()