import sys
input = sys.stdin.readline

n = int(input())
n_list = [0]*10001

for i in range(n):
  n_list[int(input())-1] += 1

for i in range(len(n_list)):
  if n_list[i] != 0:
    for j in range(n_list[i]):
      print(i+1)