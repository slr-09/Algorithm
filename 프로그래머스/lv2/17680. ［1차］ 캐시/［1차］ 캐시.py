from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque(maxlen = cacheSize)
    
    for i in cities:
        i = i.lower()
        if i in queue:
            answer += 1
            queue.remove(i)
        else:
            answer += 5
        queue.append(i)
    return answer