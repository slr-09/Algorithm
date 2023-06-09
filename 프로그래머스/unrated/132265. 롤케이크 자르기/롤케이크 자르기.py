from collections import Counter
def solution(topping):
    answer = 0
    dict = Counter(topping)
    aset=set()
    for i in topping:
        aset.add(i)
        dict[i] -= 1
        if dict[i] == 0:
            dict.pop(i)
        if len(dict) == len(aset):
            answer += 1
    return answer