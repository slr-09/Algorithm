import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

answer = 0
for i in range(n):
    if i+k<=n:
        n_set = set(n_list[i:i+k])
    else:
        n_set = set(n_list[i:n]+n_list[0:i+k-n])
    if c in n_set:
        answer = max(len(n_set), answer)
    else:
        answer = max(len(n_set)+1, answer)

print(answer)