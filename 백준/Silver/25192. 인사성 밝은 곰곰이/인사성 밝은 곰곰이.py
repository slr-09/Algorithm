import sys
input = sys.stdin.readline

n=int(input())
name = set()
answer=0
for i in range(n):
  chat = input().rstrip()
  if chat=="ENTER":
    answer += len(name)
    name = set()
  else:
    name.add(chat)
answer += len(name)

print(answer)