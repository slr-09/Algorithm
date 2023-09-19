import sys
input = sys.stdin.readline

n = int(input())
n1,n3=0,0
for i in range(1,n+1):
  n1 += i
  n3 += i*i*i

print(n1)
print(n1*n1)
print(n3)