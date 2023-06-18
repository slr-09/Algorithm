import sys
from collections import Counter
input = sys.stdin.readline

def solution(arr):
  answer = []
  num = Counter(arr)
  for i in num.values():
    if i>1:
      answer.append(i)
  if len(answer)==0:
    answer.append(-1)
  return answer

arr1 = [1,2,3,3,3,3,4,4]
arr2 = [3,2,4,4,2,5,2,5,5]
arr3 = [3,5,7,9,1]

for i in [arr1,arr2,arr3]:
  print(solution(i))
