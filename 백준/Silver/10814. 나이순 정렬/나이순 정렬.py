import sys
input = sys.stdin.readline

n = int(input())

n_list=[]
for i in range(n):
  n_list.append(list(input().split()))

n_list.sort(key=lambda x: int(x[0]))
for i in n_list:
  print(i[0],i[1])
  