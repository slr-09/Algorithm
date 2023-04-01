from collections import deque
def solution(maps):
    
    def bfs(x,y,zx,zy):
        # graph=[[] for _ in range(len(maps))]
        visited=[[False]*len(maps[0]) for _ in range(len(maps))]
        # for i in range(len(maps)):
        #     for j in range(len(maps[0])):
        #         if maps[i][j] == 'X':
        #             graph[i].append(-1)
        #         else:
        #             graph[i].append(0)
        queue=deque()
        queue.append((x,y,0))
        while queue:
            x,y,cost = queue.popleft()
            if x==zx and y==zy:
                return cost
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0]):
                    continue
                if maps[nx][ny]=='X':
                    continue
                else:
                    if not visited[nx][ny]:
                        # graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx,ny,cost+1))
                        visited[nx][ny] = True
            
        return -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = [i,j]
            elif maps[i][j] == 'E':
                e = [i,j]
            elif maps[i][j] == 'L':
                l = [i,j]
            
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    b1,b2 = bfs(s[0],s[1],l[0],l[1]),bfs(l[0],l[1],e[0],e[1])
    if b1 == -1 or b2 == -1:
        answer = -1
    else:
        answer = b1+b2
    return answer