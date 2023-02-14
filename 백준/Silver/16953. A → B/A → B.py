import sys
input = sys.stdin.readline

a,b = map(int,input().split())
count=0
while a!=b:
  if a>b:
    count=-2
    break
  if b%2==0:
    count+=1
    b = b//2
  else:
    strB=str(b)
    if strB[len(strB)-1]=='1':
      strB=strB[:len(strB)-1]
      b=int(strB)
      count+=1
    else:
      count=-2
      break

print(count+1)