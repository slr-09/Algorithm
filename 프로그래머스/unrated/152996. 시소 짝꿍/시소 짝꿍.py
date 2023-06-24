import math
from collections import Counter
def solution(weights):
    answer = 0
    num = [1/2,2/3,3/4]
    dt = Counter(weights)
    li = list(dt)
    for i in range(len(dt)):
        if dt[li[i]]==1:
            continue
        answer += dt[li[i]]*(dt[li[i]]-1)//2
    for i in range(len(li)):
        for j in num:
            if li[i]*j in li:
                answer += dt[li[i]]*dt[li[i]*j]
                
    return answer