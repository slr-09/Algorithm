def solution(order):
    container = []
    truck=[]
    i=0
    
    while True:
        if len(truck)==len(order):
            break
        
        if i+1 == order[len(truck)]:
            truck.append(i+1)
            i+=1
        elif i+1 > order[len(truck)]:
            c = container.pop()
            if c == order[len(truck)]:
                truck.append(c)
                
            else:
                break
        elif i+1 < order[len(truck)]:
            container.append(i+1)
            i += 1 
        
    return len(truck)