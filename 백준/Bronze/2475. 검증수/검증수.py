import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
sum = 0
for num in n:
  sum += num*num

print(sum%10)