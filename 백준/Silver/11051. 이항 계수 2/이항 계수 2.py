import sys
input = sys.stdin.readline

n,k = map(int,input().split())

def f(x):
    s = 1
    for i in range(1,x+1):
        s *= i

    return s

print(f(n)//(f(n-k)*f(k))%10007)