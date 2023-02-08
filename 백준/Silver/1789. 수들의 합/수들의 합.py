import sys
input = sys.stdin.readline

n = int(input())
n_set = set()
count=1
while(n):
  if n<count:  
    n_set.add(n)
    break
  n -= count
  n_set.add(count)
  count += 1
  
print(len(n_set))