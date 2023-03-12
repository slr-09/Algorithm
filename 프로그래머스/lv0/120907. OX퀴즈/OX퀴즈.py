def solution(quiz):
    answer = []
    for i in quiz:
        x,a,y,e,z = map(str,i.split())
        if a=='+':
            calculation = int(x)+int(y)
        elif a=='-':
            calculation = int(x)-int(y)
        if calculation == int(z):   answer.append("O")
        else:   answer.append("X")
    return answer