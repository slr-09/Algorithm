import sys
input = sys.stdin.readline

n = int(input())
name =  []
for i in range(n):
  name.append(list(map(str,input().split())))
name.sort(key = lambda x : (int(x[3]),int(x[2]),int(x[1])))
print(name[n-1][0])
print(name[0][0])