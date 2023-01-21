import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
a_set=set(map(int,input().split()))
b_set=set(map(int,input().split()))

a = a_set-b_set
b = b_set-a_set

print(len(a)+len(b))