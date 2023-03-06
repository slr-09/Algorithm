import sys
input = sys.stdin.readline

n=[]
sum=0
for i in range(8):
  n.append(int(input()))

n_list = sorted(n)
num = n_list[3]
pr=set()
for i in range(8):
  if n[i]>=num:
    sum += n[i]
    pr.add(i+1)
print(sum)
for i in pr:
  print(i,end=" ")
