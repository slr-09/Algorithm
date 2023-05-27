import math
def solution(arrayA, arrayB):
    gcdA,gcdB = 0,0

    for i in range(len(arrayA)):
        gcdA = math.gcd(gcdA,arrayA[i])
        gcdB = math.gcd(gcdB,arrayB[i])
        
    for i in range(len(arrayA)):
        if arrayA[i]%gcdB == 0:
            gcdB=1
        if arrayB[i]%gcdA == 0:
            gcdA=1
    
    if gcdA==1 and gcdB==1:
        return 0
    else:
        return  max(gcdA,gcdB)
    