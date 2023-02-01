import sys
input = sys.stdin.readline

while(1):
  num=input().strip()
  if num=="0":  break
  for i in range(int(len(num)/2)+1):
      if i==int(len(num)/2):
        print("yes")
        break
      if num[i]==num[len(num)-i-1]:
        continue
      else:  
        print("no")
        break
    