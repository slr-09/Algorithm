import sys
input = sys.stdin.readline

x = int(input())
xlist = [64]

while True: 
  s = sum(xlist)
  if s == x:
    break
  m = min(xlist)
  xlist.remove(m)
  xlist.append(m//2)
  if s - m//2 < x: 
    xlist.append(m//2)

print(len(xlist))