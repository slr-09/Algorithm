import sys
input = sys.stdin.readline

n = int(input())
n_set = set(map(int,input().split()))
n_list = sorted(list(n_set))
for i in n_list:
  print(i,end=" ")