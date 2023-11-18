import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
d = [0]*100001
answer = 0

def f(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v==k:
            global answer
            answer += 1
            continue
        for i in (v-1, v+1, v*2):
            if 0<=i<100001 and (d[i]==0 or d[i]==d[v]+1):
                d[i] = d[v]+1
                queue.append(i)
        
f(n)
print(d[k])
print(answer)