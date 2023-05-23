def solution(storey):
    answer = 0
    num = len(str(storey))
    
    while storey:
        storey,r = divmod(storey,10)
        if r>5 or (r==5 and storey%10>=5):
            answer += 10-r
            storey += 1
        else:
            answer += r
        
    return answer