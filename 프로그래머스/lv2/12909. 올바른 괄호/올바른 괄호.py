def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        elif i==')':
            if len(stack)==0 or stack.pop() != '(':
                return False
    if len(stack) > 0:
        return False
    return True