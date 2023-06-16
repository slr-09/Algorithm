import sys
input = sys.stdin.readline

n,k = map(int,input().split())
value = [int(input()) for _ in range(n)]

d = [0] * (k+1)
d[0] = 1  # 동전을 하나만 쓰는 경우를 고려

for i in value:
  for j in range(i,k+1):
    # i원짜리 동전으로 j원 만들기 -> j-i원을 만든 후 i원을 더하는 것과 같음
    # -> d[j-i]와 같음
    d[j] += d[j-i]

print(d[k])