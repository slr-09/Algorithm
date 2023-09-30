import sys
input = sys.stdin.readline

a = input().rstrip()
if int(a)%30 == 0:
  print(a)
elif "0" not in a:
  print(-1)
else:
  sum = 0
  for i in a:
    sum += int(i)
  if sum%3 != 0:
    print(-1)
  else:
    x = sorted(a, reverse=True)
    result = ''.join(x)
    print(result)