def solution(players, callings):
    d=dict()
    for i,j in enumerate(players):
        d[j] = i
    for i in callings:
        idx = d[i]
        players[idx], players[idx-1] = players[idx-1], players[idx] 
        d[players[idx-1]] , d[players[idx]] = d[players[idx-1]] - 1 , d[players[idx]] + 1
    return players