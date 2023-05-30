import sys
input = sys.stdin.readline

n=int(input())
n_dict={}
str=[]
for i in range(26):
  n_dict[chr(65+i)] = 0

for i in range(n):
  s = input().rstrip()
  str.append(s)
  for j in range(len(s)):
    n_dict[s[j]] += 10**(len(s)-1-j)

n_dict = sorted(n_dict.items(),key=lambda x:x[1], reverse=True)
new = {}
for i in range(10):
  new[n_dict[i][0]] = 9-i

num = 0
for i in range(n):
  for j in range(len(str[i])):
    num += new[str[i][j]]*10**(len(str[i])-j-1)

print(num)