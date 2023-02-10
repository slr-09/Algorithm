import sys
input = sys.stdin.readline

n=int(input())
count=0
if n<=1 or n==3:
  print(-1)
elif n<5:
  print(n//2)
else:
  count += n//5
  n %= 5
  if n%2 != 0 and count>0:
    count -= 1
    n += 5
  
  count += n//2
  print(count)