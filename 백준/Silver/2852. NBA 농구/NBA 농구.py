import sys
from datetime import datetime
input = sys.stdin.readline

n = int(input())

pretime = datetime.strptime("00:00", "%M:%S")
endtime = datetime.strptime("48:00","%M:%S")
team1 = datetime.strptime("00:00", "%M:%S")
team2 = datetime.strptime("00:00", "%M:%S")
score = [0,0]

n_list = []
for i in range(n):
    team, time = map(str, input().rstrip().split())
    tt = datetime.strptime(time, "%M:%S")
    n_list.append([team, tt-pretime])
    pretime = tt

n_list.append([0, endtime-pretime])

for i in range(n):
    if n_list[i][0] == '1':
        score[0] += 1
    elif n_list[i][0] == '2':
        score[1] += 1

    if score[0] > score[1]:
        team1 += n_list[i+1][1]
    elif score[0] < score[1]:
        team2 += n_list[i+1][1]
    else:
        continue

print(datetime.strftime(team1, "%M:%S"))
print(datetime.strftime(team2, "%M:%S"))