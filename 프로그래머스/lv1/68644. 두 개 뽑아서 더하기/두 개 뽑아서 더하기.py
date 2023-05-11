def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if not numbers[i]+numbers[j] in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer