def solution(cards):
    answer = 0
    idx,num=0,0
    group=[]
    number=[i for i in range(len(cards))]

    while True:
        if cards[idx]==0:
            group.append(num)
            num=0
            if len(number)>0:
                idx = number[0] 
                continue
            break
        if len(number)==0:
            break
        x = cards[idx]
        cards[idx] = 0
        idx = x-1
        
        number.remove(idx)
        num += 1
        
    group.sort(reverse=True)

    if len(group)<2:
        return 0
    return group[0]*group[1]