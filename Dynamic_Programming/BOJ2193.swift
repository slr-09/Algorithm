import Foundation

let n = Int(readLine()!)!
var d: [[Int]] = Array(repeating: [0,0], count: n+1)

d[1] = [0,1]
if n > 1 {
    d[2] = [1,0]
}

if n > 2 {
    for i in 3..<n+1 {
        d[i] = [d[i-1][0]+d[i-1][1], d[i-1][0]]
    }
}

print(d[n][0]+d[n][1])
