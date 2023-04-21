def solution(k, tangerine):
    answer = 0
    dict={}
    for i in tangerine:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    sum=0
    for i in dict:
        if sum >= k:    break
        sum += i[1]
        answer += 1
    return answer