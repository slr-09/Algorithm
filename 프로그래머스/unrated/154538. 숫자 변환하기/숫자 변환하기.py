from collections import deque
def solution(x, y, n):
    
    d = [0 for _ in range(y+1)]

    q = deque([x])
    while q:
        v = q.popleft()
        if v==y:
            return d[y]
        for i in [v+n,v*2,v*3]:
            if i<y+1 and not d[i]:
                d[i] = d[v]+1
                q.append(i)
                
    return -1