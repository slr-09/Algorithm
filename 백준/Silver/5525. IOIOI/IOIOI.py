[100점]
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
str = input().rstrip()

i,cnt,answer = 0,0,0
while i<=m-2:
  if str[i:i+3] == "IOI":
    i += 2
    cnt += 1
    if cnt == n:
      cnt -= 1
      answer += 1
  else:
    i += 1
    cnt = 0 

print(answer)

-------------------------
[50점]
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
