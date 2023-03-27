def solution(my_string):
    answer = my_string.lower()
    li=list(answer)
    li.sort()
    answer = ''.join(li)
    return answer