import sys
input = sys.stdin.readline

n=input()
n_set = set()

for i in range(1,len(n)):
  for j in range(len(n)):
    if i+j>=len(n):  break
    n_set.add(n[j:i+j])

print(len(n_set))