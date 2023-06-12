import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node:
  def __init__(self,data,left,right):
    self.data = data
    self.left = left
    self.right = right

n = int(input())
tree = {}
root = [0]*(n+1)
for i in range(n):
  data,left,right = map(int,input().split())
  if left == -1:
    left = 0
  else:
    root[left] = data
  if right == -1:
    right = 0
  else:
    root[right] = data
  tree[data] = Node(data,left,right)

inlist = []

def in_order(node):
  if node.left != 0:
    in_order(tree[node.left])
  inlist.append(node.data)
  if node.right != 0:
    in_order(tree[node.right])

in_order(tree[1])
end = inlist[-1]
visited=[False]*(n+1)
count = -1

def order(node):
  visited[node.data] = True
  global count
  count += 1
  
  if node.left != 0 and not visited[node.left]:
    order(tree[node.left])
  elif node.right != 0 and not visited[node.right]:
    order(tree[node.right])
  elif node.data == end:
    return 
  elif root[node.data] != 0:
    order(tree[root[node.data]])

order(tree[1])
print(count)