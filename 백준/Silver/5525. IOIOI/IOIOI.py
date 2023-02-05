import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
str = input()
n_list = []

for i in range(n):
  n_list.append("I")
  n_list.append("O")
n_list.append("I")

str2 = ''.join(n_list)
num = set()
for i in range(m):
  index = str.find(str2, i, m)
  if index!=-1 and index not in num:
    num.add(index)

print(len(num))