import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_list=sorted(list(map(int,input().split())))
m_list=sorted(list(map(int,input().split())))
nm=sorted(n_list+m_list)
for i in nm:
  print(i,end=" ")