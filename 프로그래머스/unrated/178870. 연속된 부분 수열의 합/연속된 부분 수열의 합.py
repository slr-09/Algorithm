def solution(sequence, k):
    answer = []
    sum=0
    stidx=0
    edidx=-1
    while True:
        if sum < k:
            edidx += 1
            if edidx >= len(sequence):  break
            sum += sequence[edidx]
        else:
            sum -= sequence[stidx]
            if stidx >= len(sequence):  break
            stidx += 1
            
        if sum == k:
            answer.append([stidx,edidx])
            
    answer.sort(key=lambda x : (x[1]-x[0],x[0]))
    
    return answer[0]