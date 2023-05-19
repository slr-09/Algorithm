import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    num=0
    for i in enemy:
        heapq.heappush(heap,-i)
        num += i
        if num>n:
            if k==0: break
            num += heapq.heappop(heap)
            k -= 1
        answer += 1
        

    # for i in range(len(enemy)):
    #     num += enemy[i]
    #     heapq.heappush(heap,-enemy[i])
    #     if num >= n and k>0:
    #         num += heapq.heappop(heap)
    #         k -= 1
    #     elif num > n and k==0:
    #         answer = i
    #         break
    #     elif num == n and k==0:
    #         answer = i+1
    #         break
    #     answer = i+1
    
    return answer