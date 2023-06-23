def solution(s):
    answer = [0,0]
    while s!="1":
        for _ in range(len(s)):
            if '0' in s:
                s = s.replace("0","",1)
                answer[1] += 1
            else:
                break
        n = len(s)
        num=[]
        while n:
            num.append(str(n%2))
            n //= 2
        num.reverse()
        s = ''.join(num)
        answer[0] += 1
    return answer