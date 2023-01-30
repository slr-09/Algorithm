import sys
input = sys.stdin.readline

n_num = [0]*41
n_count = [[0]*2 for i in range(41)]
def fibonacci(n):
    if (n <= 1):
      return n
    if n_num[n] != 0:
      return n_num[n]
    
    n_num[n] = fibonacci(n-1) + fibonacci(n-2)
    n_count[n][0] = n_count[n-1][0] + n_count[n-2][0]
    n_count[n][1] = n_count[n-1][1] + n_count[n-2][1]
    return n_num[n]

n = int(input())
n_num[1]=1
n_count[0][0] = 1
n_count[1][1] = 1

for i in range(n):
  num=int(input())
  fibonacci(num)
  print(n_count[num][0],n_count[num][1])