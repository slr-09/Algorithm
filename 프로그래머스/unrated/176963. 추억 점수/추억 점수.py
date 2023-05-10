def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    for i in range(len(photo)): 
        for j in range(len(name)):
            if name[j] in photo[i]:
                answer[i] += yearning[j]
                
    return answer