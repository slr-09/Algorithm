import sys
input = sys.stdin.readline

n,c = map(int,input().split())
n_list = list(map(int,input().split()))
n_dict = dict()
for i in n_list:
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

sorted_dict = sorted(n_dict.items(), key=lambda x:x[1], reverse=True)

for i in range(len(sorted_dict)):
    a,b = sorted_dict[i]
    for j in range(b):
        print(a, end=" ")