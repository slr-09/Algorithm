import sys
input = sys.stdin.readline

n_list = []
sum=0
for i in range(5):
  num=int(input())
  n_list.append(num)
  sum += num

n_list.sort()

print(int(sum/5))
print(n_list[2])