import sys
input = sys.stdin.readline

n = int(input())
s=set()
for i in range(n):
  m = list(map(str,input().split()))
  if m[0]=="add":
    s.add(int(m[1]))
  elif m[0]=="remove":
    s.discard(int(m[1]))
  elif m[0]=="check":
    if int(m[1]) in s:
      print("1")
    else:
      print("0")
  elif m[0]=="toggle":
    if int(m[1]) in s:
      s.remove(int(m[1]))
    else:
      s.add(int(m[1]))
  elif m[0]=="all":
    s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
  elif m[0]=="empty":
    s=set()
