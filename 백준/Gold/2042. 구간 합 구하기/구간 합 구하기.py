import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = [0]*(n+1)
tree = [0]*(n+1)

# i까지의 누적 합
def prefix_sum(i):
  result = 0
  while i>0:
    result += tree[i]
    i -= (i&-i)
  return result

# i번째 수를 d만큼 더하는 함수
def update(i,d):
  while i<=n:
    tree[i] += d
    i += (i&-i)

# start부터 end까지 구간 합
def interval_sum(start,end):
  return prefix_sum(end) - prefix_sum(start-1)

for i in range(1,n+1):
  x = int(input())
  arr[i] = x
  update(i,x)

for _ in range(m+k):
  a,b,c = map(int,input().split())
  if a==1:
    update(b,c-arr[b])
    arr[b] = c
  elif a==2:
    print(interval_sum(b,c))
    