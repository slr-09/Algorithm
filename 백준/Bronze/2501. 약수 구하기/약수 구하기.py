import sys
input = sys.stdin.readline

n,k = map(int,input().split())
c,answer=0,0
for i in range(n):
  if n%(i+1)==0:
    c+=1
  if c==k:  
    answer = i+1
    break

print(answer)