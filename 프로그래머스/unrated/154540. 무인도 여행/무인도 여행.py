import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    answer = []
    global graph
    graph=[]
    for i in range(len(maps)):
        graph.append([])
        graph[i] = list(maps[i])
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            global num
            num=0
            if dfs(i,j) == True:
                answer.append(num)
    if len(answer)==0:  answer.append(-1)
    else: answer.sort()
    
    return answer

def dfs(x,y):
    global graph
    if x<0 or x>=len(graph) or y<0 or y>=len(graph[0]):
        return False
    if graph[x][y] != 'X':
        global num
        num += int(graph[x][y])
        graph[x][y] = 'X'
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False