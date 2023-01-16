import sys
input = sys.stdin.readline

n_list=[]
for i in range(30):
  n_list.append(i+1)

for i in range(28):
  n_list.remove(int(input()))

for i in n_list:
  print(i)