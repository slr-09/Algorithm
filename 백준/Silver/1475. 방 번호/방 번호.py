import sys
input = sys.stdin.readline

n=int(input())
n_list=[0 for _ in range(10)]
n = str(n)
for i in range(len(n)):
  if n[i]=='6' or n[i]=='9':
    if n_list[6]>n_list[9]:
      n_list[9] += 1
    else:
      n_list[6] += 1
  else:
    n_list[int(n[i])] += 1

print(max(n_list))