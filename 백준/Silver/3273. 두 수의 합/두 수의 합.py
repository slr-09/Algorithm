import sys
input = sys.stdin.readline

n=int(input())
n_list = list(map(int,input().split()))
x=int(input())

n_list.sort()
left, right = 0, n-1
count=0
while left<right:
  tmp = n_list[left] + n_list[right]
  if tmp==x:  count += 1
  if tmp<x:
    left += 1
    continue
  right -= 1

print(count)