import Foundation

let ns = readLine()!.split(separator: " ").map{Int($0)!}
let (n,s) = (ns[0],ns[1])
let arr: [Int] = readLine()!.split(separator: " ").map{Int($0)!}

var (st,ed) = (0,0)
var sum = 0
var minCount = Int.max
while ed < n {
    sum += arr[ed]
    
    // sum이 s 이상이라면
    while sum >= s {
        minCount = min(minCount, ed-st+1)
        
        sum -= arr[st]
        st += 1
    }
    
    ed += 1
}
print(minCount == Int.max ? 0 : minCount)
