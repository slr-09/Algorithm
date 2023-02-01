import sys
input = sys.stdin.readline

T=int(input())
for i in range(T):
  n_list=[]
  n=int(input())
  count=1
  for j in range(n):
    n_list.append(list(map(int,input().split())))
  n_list.sort()

  minn = n_list[0][1]
  for j in range(n):
    my = n_list[j][1]
    if minn > my:
      minn=my
      count += 1
  print(count)
  