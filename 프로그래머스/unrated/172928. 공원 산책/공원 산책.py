def solution(park, routes):
    answer = []
    h,w=len(park), len(park[0])
    x_list=[]
    for i in range(h):
        for j in range(w):
            if park[i][j]=='S':
                x=i
                y=j
            elif park[i][j]=='X':
                x_list.append([i,j])
            
    for i in range(len(routes)):
        dx,dy = 0,0
        op, n = map(str,routes[i].split())
        check=True
        for j in range(1,int(n)+1):
            if op=='N':
                if [x-j,y] in x_list:
                    check=False
                    break
                else:
                    dx -= 1
            elif op=='S':
                if [x+j,y] in x_list:
                    check=False
                    break
                else: 
                    dx += 1
            elif op=='W':
                if [x,y-j] in x_list:
                    check=False
                    break
                else: 
                    dy -= 1
            elif op=='E':
                if [x,y+j] in x_list:
                    check=False
                    break
                else:
                    dy += 1
        if x+dx<0 or x+dx>=h or y+dy<0 or y+dy>=w:
            continue
        if check:
            x += dx
            y += dy

    answer.append(x)
    answer.append(y)
    return answer