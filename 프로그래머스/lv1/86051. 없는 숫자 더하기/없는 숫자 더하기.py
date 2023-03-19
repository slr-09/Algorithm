def solution(numbers):
    answer = 0
    li=[0,1,2,3,4,5,6,7,8,9]
    for i in li:
        if i not in numbers:
            answer += i
    return answer