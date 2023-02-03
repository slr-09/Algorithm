import sys
input = sys.stdin.readline

while(1):
  n_list=[]
  n = input()
  if n == ".\n":  break
  n = n.replace(" ","")
  for i in range(len(n)):
    if n[i]=="(":
      n_list.append("(")
    elif n[i]=="[":
      n_list.append("[")
    elif n[i]==")":
      if len(n_list)==0:
        n_list.append(")")
        break
      if n_list[-1]=="(":
        n_list.pop(-1)
      elif n_list[-1]=="[":
        break
    elif n[i]=="]":
      if len(n_list)==0:
        n_list.append("]")
        break
      if n_list[-1]=="[":
        n_list.pop(-1)
      elif n_list[-1]=="(":
        break
    else:  continue
  if len(n_list)==0:  
    print("yes")
  else:
    print("no")


