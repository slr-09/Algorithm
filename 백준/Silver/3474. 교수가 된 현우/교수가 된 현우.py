import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = 0
    n = int(input())
    t = 5
    while t<=n:
        num += n//t
        t *= 5
        
    print(num)