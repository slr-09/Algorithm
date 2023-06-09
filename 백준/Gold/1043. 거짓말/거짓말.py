import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
people = set(map(int,input().split()[1:]))

count=0
party=[]
for _ in range(m):
  party.append(set(map(int,input().split()[1:])))

for _ in range(m):
  for i in party:
    if i & people:
      people = people.union(i)

for i in party:
  if i&people:
    continue
  count += 1

print(count)