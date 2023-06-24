import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
st = list(map(int,input().split()))
dt = {}

for i in st:
  if i in dt.keys():
    dt[i] += 1
  else:
    if len(dt)>=n:
      dt2 = sorted(dt.items(),key=lambda x:x[1])
      dt.pop(dt2[0][0])
    dt[i] = 1
    
dt=sorted(dt.keys())
print(*dt)