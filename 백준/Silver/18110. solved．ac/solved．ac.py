import sys
input = sys.stdin.readline

n = int(input())
if n==0:
    print(0)
else:
    num = int(n*0.15+0.5)
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))

    n_list.sort()
    for i in range(num):
        n_list[i] = 0
        n_list[n-i-1] = 0

    print(int(sum(n_list)/(n-2*num)+0.5))