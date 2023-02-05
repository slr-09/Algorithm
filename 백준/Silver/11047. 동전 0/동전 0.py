import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
n_list = []
for i in range(n[0]):
  n_list.append(int(input()))
count=0
for i in range(n[0]):
  if n[1]/n_list[n[0]-i-1]>0:
    count += int(n[1]/n_list[n[0]-i-1])
    n[1] %= n_list[n[0]-i-1]
  if int(n[1])==0:
    break

print(count)