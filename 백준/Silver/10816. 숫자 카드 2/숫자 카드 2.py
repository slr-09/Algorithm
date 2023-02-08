import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))
n_dict = {}
for i in range(n):
  count=1
  if n_list[i] in n_dict:
    count = n_dict[n_list[i]] + 1
  n_dict[n_list[i]] = count
answer=[]
for i in m_list:
  if i in n_dict:
    answer.append(n_dict[i])
  else:
    answer.append(0)

for i in answer:
  print(i,end=" ")
  