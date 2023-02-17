import sys
input = sys.stdin.readline

s=input()
str=[]
for i in range(len(s)-1):
  str.append(s[i:len(s)-1])

str.sort()
for i in str:
  print(i)
