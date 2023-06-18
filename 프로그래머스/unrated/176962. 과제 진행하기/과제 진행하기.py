
def solution(plans):
    answer = []
    plans.sort(key = lambda x: x[1])
    study = []
    idx=0
    while len(answer) != len(plans):
        h,m = map(int,plans[idx][1].split(':'))
        if idx != len(plans)-1:
            hh,mm = map(int,plans[idx+1][1].split(':'))
            c = (hh-h)*60 + mm - m  # 다음 과제 시작 시간과 현재 과제 시작시간 차이
            if c >= int(plans[idx][2]):
                answer.append(plans[idx][0])
                c -= int(plans[idx][2])
                for i in range(len(study)):
                    a,b = study.pop()
                    if b > c:
                        study.append((a,b-c))
                        break
                    elif b==c:
                        answer.append(a)
                        break
                    else:
                        answer.append(a)
                        c -= b
            else:
                study.append((plans[idx][0],int(plans[idx][2])-c))
        else:
            answer.append(plans[idx][0])
            for i in range(len(study)):
                answer.append(study.pop()[0])
        idx += 1
                    
            
    return answer