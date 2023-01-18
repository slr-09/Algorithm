def solution(n):
    answer = 0
    for i in range(n):
        num = n%(i+1)
        if num==0:
            answer += i+1
    
    return answer