import sys
input = sys.stdin.readline

arr = [("BOOL",1),("SHORT",2),("FLOAT",4),("INT",8),("LONG",8)]

def solution(input):
  answer = ''
  coma = 0
  for i in input:
    if (len(answer)-coma)%8==0 and len(answer)!=0:
      answer += ','
      coma += 1
    for j in arr:
      if i!=j[0]:
        continue
      while len(answer.replace(',',''))%j[1]:
          answer += '.'
      if (len(answer)-coma)%8==0 and coma != len(answer)//8 and len(answer)!=0:
        answer += ','
        coma += 1
      if j[0] == "LONG":
        answer += "########,########"
        continue
      for k in range(j[1]):
        answer += '#'
      break
    if len(answer.replace(',',''))>128:
      return "HALT"
  while len(answer.replace(',',''))%8:
    answer += '.'
  return answer

test1 = ["INT","INT","BOOL","SHORT","LONG"]
test2 = ["INT","SHORT","FLOAT","INT","BOOL"]
test3 = ["FLOAT","SHORT","BOOL","BOOL","BOOL","INT"]
test4 = ["BOOL","LONG","SHORT","LONG","BOOL","LONG","BOOL","LONG","SHORT","LONG","LONG"]

for i in [test1,test2,test3,test4]:
  print(solution(i))
