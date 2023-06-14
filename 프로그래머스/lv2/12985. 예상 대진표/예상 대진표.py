def solution(n,a,b):
    answer = 0

    while True:
        if abs(a-b)==1:
            if (a>b and a%2==0) or (a<b and b%2==0):
                answer += 1
                break
        answer += 1
        a = (a+1)//2
        b = (b+1)//2
        
    return answer