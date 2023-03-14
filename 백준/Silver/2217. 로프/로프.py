import sys
input = sys.stdin.readline

n=int(input())
n_list=[]
for i in range(n):
  n_list.append(int(input()))
n_list.sort(reverse=True)
answer=[]
for i in range(n):
  answer.append(n_list[i]*(i+1))
print(max(answer))