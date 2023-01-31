import sys
input = sys.stdin.readline

n=int(input())
n_list = list(map(int,input().split()))

n_list.sort()

if n==1:
  answer = n_list[0]*n_list[0]
else:
  answer = n_list[0]*n_list[-1]

print(answer)