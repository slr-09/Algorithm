import sys
input = sys.stdin.readline

n = int(input())
n_list=[]
for i in range(n):
  n_list.append(list(map(int,input().split())))

n_list.sort(key=lambda x: (x[1],x[0]))
count=1

endTime = n_list[0][1]
n_list.pop(0)

i=0
while(len(n_list)):
  if i==len(n_list): break
  if n_list[i][0]>=endTime:
    count += 1
    endTime = n_list[i][1]
    n_list.pop(i)
    i=-1
  i += 1

print(count)