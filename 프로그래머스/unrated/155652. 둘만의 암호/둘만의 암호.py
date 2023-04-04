from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    alpha=list(ascii_lowercase)
    for i in range(len(skip)):
        alpha.remove(skip[i])
    
    for i in range(len(s)):
        idx = alpha.index(s[i])
        idx = (idx+index)%len(alpha)
        
        answer += alpha[idx]
        
    return answer