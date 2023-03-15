def solution(array, n):
    minNum = 100
    array.sort()
    for i in array:
        if abs(n-i)<minNum:
            minNum = abs(n-i)
            answer = i
            
    return answer