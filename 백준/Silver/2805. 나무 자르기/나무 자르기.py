import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_list = list(map(int,input().split()))

start=0
end=max(n_list)

while start<=end:
  total=0
  mid = (start+end)//2
  for x in n_list:
    if x>mid:
      total += x-mid

  if total<m:
    end = mid-1
  else:
    start = mid+1
    
print(end)
