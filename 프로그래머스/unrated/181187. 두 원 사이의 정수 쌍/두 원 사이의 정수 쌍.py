from math import sqrt,ceil,floor
def solution(r1, r2):
    answer = 0 
    for x in range(1,r2+1):
        maxy = floor(sqrt(r2**2-x**2))
        if x>r1: miny=0
        else:   miny=ceil(sqrt(r1**2-x**2))
        answer += maxy-miny+1
    
    return answer*4