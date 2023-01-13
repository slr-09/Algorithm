import sys
input = sys.stdin.readline

n = int(input())

n_set = set()
for i in range(n):
  n_set.add(input())
n_list = list(n_set)
n_list.sort(key=lambda x : (len(x),x))

for i in n_list:
  print(i, end="")
  