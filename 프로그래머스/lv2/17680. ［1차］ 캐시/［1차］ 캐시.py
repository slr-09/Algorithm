from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    if cacheSize == 0:
        return 5*len(cities)
    for i in cities:
        i = i.lower()
        if i in queue:
            answer += 1
            queue.remove(i)
        else:
            answer += 5
            if len(queue)>=cacheSize: 
                queue.popleft()
        queue.append(i)
    return answer