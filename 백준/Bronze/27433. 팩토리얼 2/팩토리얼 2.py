import sys
input = sys.stdin.readline

n=int(input())

def f(n):
  if n==0 or n==1: return 1
  return n*f(n-1)

print(f(n))