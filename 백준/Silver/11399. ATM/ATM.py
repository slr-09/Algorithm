import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int,input().split())))
num = 0
total = 0
for i in n_list:
  num += i
  total += num

print(total)