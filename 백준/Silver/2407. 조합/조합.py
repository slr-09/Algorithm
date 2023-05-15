import sys
input = sys.stdin.readline

n,m=map(int,input().split())
num1=1
num2=1
for i in range(m):
  num1 *= n-i
  num2 *= m-i

print(num1//num2)