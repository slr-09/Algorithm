def solution(board):
    answer = 1
    o = []
    x = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="O":
                o.append((i,j))
            elif board[i][j]=="X":
                x.append((i,j))
    
    if len(o) < len(x) or len(o) - len(x)>1:
        return 0

    ch=False
    ch2=False
    for i in range(len(board)):
        if board[0][i]==board[1][i]==board[2][i] == "O":
            ch = True
        elif board[0][i]==board[1][i]==board[2][i] == "X":
            ch2 = True
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]=="O":
            ch = True
        elif board[i][0]==board[i][1]==board[i][2] and board[i][0]=="X":
            ch2 = True
        
    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0]=="O":
            ch = True
        elif board[0][0]=="X":
            ch2 = True
    if board[0][2]==board[1][1]==board[2][0]:
        if board[0][2]=="O":
            ch = True
        elif board[0][2]=="X":
            ch2=True
    
    
    if ch==True and len(o) == len(x):
        return 0
    if ch2==True and len(o) > len(x):
        return 0
    if ch==True and ch2==True:
        return 0
    return answer