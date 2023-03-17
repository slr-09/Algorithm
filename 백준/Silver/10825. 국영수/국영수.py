import sys
input = sys.stdin.readline

n = int(input())
n_list=[]
for i in range(n):
 n_list.append(list(map(str,input().split())))

n_list.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
  print(n_list[i][0])