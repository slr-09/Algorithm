import sys
input = sys.stdin.readline

n=int(input())
book = dict()
for i in range(n):
  title = input()
  if title in book:
    book[title] += 1
  else:
    book[title] = 1

book = sorted(book.items(), key=lambda x:(-x[1],x[0]))
print(book[0][0],end="")
