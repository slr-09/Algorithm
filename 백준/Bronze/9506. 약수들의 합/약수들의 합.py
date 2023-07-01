import sys
input = sys.stdin.readline

while True:
  n= int(input())
  if n==-1:
    break
  nn=[]
  for i in range(1,n):
    if n%(i)==0:
      nn.append(i)
  
  if sum(nn)==n:
    print(n,"="," + ".join(map(str,nn)))
  else:
    print(n,"is NOT perfect.")