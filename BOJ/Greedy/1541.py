import sys
input = sys.stdin.readline

str = list(map(str,input().rstrip().split('-')))

for i in range(len(str)):
  if '+' in str[i]:
    sum=0
    num = list(map(int,str[i].split('+')))
    for j in num:
      sum += j
    str[i] = sum
  else: 
    str[i] = int(str[i])

answer=str[0]
for i in range(1,len(str)):
  answer -= str[i]
print(answer)
