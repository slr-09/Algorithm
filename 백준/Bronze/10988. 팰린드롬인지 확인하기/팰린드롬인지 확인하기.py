import sys
input = sys.stdin.readline

str = input().rstrip()
result = 1
for i in range(len(str)//2):
  if str[i] != str[len(str)-i-1]:
    result = 0
    break
print(result)