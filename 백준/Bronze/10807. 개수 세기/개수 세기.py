import sys
input = sys.stdin.readline

n = int(input())
n_list=list(map(int,input().split()))
x=int(input())
count=0
for i in n_list:
  if i==x:
    count += 1
print(count)