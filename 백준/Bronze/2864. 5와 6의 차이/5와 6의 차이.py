import sys
input = sys.stdin.readline

a = list(input().split())
maxNum=[]
minNum=[]

for i in a[0]:
  if i=='5' or i=='6':
    maxNum.append('6')
    minNum.append('5')
  else:
    maxNum.append(i)
    minNum.append(i)

n1 = int(''.join(minNum))
n2 = int(''.join(maxNum))

maxNum.clear()
minNum.clear()

for i in a[1]:
  if i=='5' or i=='6':
    maxNum.append('6')
    minNum.append('5')
  else:
    maxNum.append(i)
    minNum.append(i)

n1 += int(''.join(minNum))
n2 += int(''.join(maxNum))

print(n1,n2)