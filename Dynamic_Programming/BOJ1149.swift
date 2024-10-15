import Foundation

let n = Int(readLine()!)!
var d: [[Int]] = Array(repeating: [0,0,0], count: n)
var arr: [[Int]] = []
for _ in 0..<n {
    arr.append(readLine()!.split(separator: " ").map{Int($0)!})
}

d[0] = arr[0]

for i in 1..<n {
    let prev = d[i-1]
    let red = min(prev[1], prev[2]) + arr[i][0]
    let green = min(prev[0], prev[2]) + arr[i][1]
    let blue = min(prev[0], prev[1]) + arr[i][2]
    
    d[i] = [red, green, blue]
}

print(d[n-1].min()!)
