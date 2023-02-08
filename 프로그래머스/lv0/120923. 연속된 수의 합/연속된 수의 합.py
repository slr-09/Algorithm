def solution(num, total):
    answer = []
    if num%2==0:
        for i in range(1,num//2):
            answer.append(total//num-i)
            answer.append(total//num+i)
        answer.append(total//num+num//2)
        
    else:
        for i in range(1, num//2+1):
            answer.append(total//num-i)
            answer.append(total//num+i)
    answer.append(total//num)
    answer.sort()
    return answer