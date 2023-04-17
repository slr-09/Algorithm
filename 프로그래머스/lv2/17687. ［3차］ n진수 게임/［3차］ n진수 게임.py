def solution(n, t, m, p):
    answer = ''
    
    def convert(num,base):
        T = "0123456789ABCDEF"
        q,r = divmod(num,base)
        if q==0:
            return T[r]
        else:
            return convert(q,base) + T[r] 
    
    st = ''
    for i in range(t*m):
        st += str(convert(i,n))
    
    while len(answer)<t:
        answer += st[p-1]
        p += m
        
    return answer