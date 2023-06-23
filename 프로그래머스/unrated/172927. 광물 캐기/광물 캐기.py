def solution(picks, minerals):
    answer = 0
    s = sum(picks)
    value=[[0]*3 for _ in range(len(minerals)//5+1)]
    for i in range(len(minerals)):
        if s*5 < i+1:
            break
        value[i//5][0] += 1
        if minerals[i]=="diamond":
            value[i//5][1] += 5
            value[i//5][2] += 25
        elif minerals[i]=="iron":
            value[i//5][1] += 1
            value[i//5][2] += 5
        elif minerals[i]=="stone":
            value[i//5][1] += 1
            value[i//5][2] += 1
    value.sort(key=lambda x:(x[2],x[1]), reverse=True)
    
    for i in range(s):
        if i >= len(value):
            break
        for j in range(3):
            if picks[j] == 0:
                continue
            elif picks[j] > 0:
                answer += value[i][j]
                picks[j] -= 1
                break
    return answer