import sys
input = sys.stdin.readline

name = input().rstrip()
dict={}
for i in range(len(name)):
  if name[i] in dict:
    dict[name[i]] += 1
  else:
    dict[name[i]] = 1

dict = sorted(dict.items())
answer = []
check=False
st=''
for i in range(len(dict)):
  if len(name)==1: break
  for j in range(dict[i][1]//2):
      answer.append(dict[i][0])
  if dict[i][1]%2 == 1 and not check:
    st = dict[i][0]
    check = True
  elif dict[i][1]%2 == 1 and check:
    answer = []
    break
  
copy = sorted(answer,reverse=True)

if len(name)==1:
  print(name)
elif len(answer):
  answer.append(st)
  print(''.join(answer)+''.join(copy))
else:
  print("I'm Sorry Hansoo")