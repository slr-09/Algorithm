import sys
input = sys.stdin.readline

n=1000-int(input())
arr = [500,100,50,10,5,1]
count=0
for i in range(len(arr)):
  count += n//arr[i]
  n = n%arr[i]

print(count)