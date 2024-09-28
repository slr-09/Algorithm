import Foundation

let nk = readLine()!.split(separator: " ").map{Int($0)!}
let (n,k) = (nk[0],nk[1])
var time = Array(repeating: 100001, count: 100001)
var visited = Array(repeating: false, count: 100001)
time[n] = 0

var queue = [n]
while !queue.isEmpty {
    let l = queue.removeFirst()
    
    if l == k { break }
    
    for i in [2*l,l-1,l+1] {
        if !(0..<time.count ~= i) { continue }
        if visited[i] { continue }
        
        if i == 2*l {
            time[i] = time[l]
        } else {
            time[i] = min(time[i], time[l]+1)
        }
        
        visited[i] = true
        queue.append(i)
    }
}

print(time[k])
