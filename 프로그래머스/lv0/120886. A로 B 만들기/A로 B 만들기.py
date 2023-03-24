def solution(before, after):
    answer = 0
    a_list = list(after)
    for i in range(len(before)):
        if before[i] in a_list:
            a_list.remove(before[i])
    if len(a_list) == 0:    answer=1
    return answer