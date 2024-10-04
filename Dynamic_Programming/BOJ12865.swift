import Foundation

let nk = readLine()!.split(separator: " ").map{Int($0)!}
var arr: [[Int]] = [[0,0]]
for _ in 0..<nk[0] {
    arr.append(readLine()!.split(separator: " ").map{Int($0)!})
}

var d: [[Int]] = Array(repeating: Array(repeating: 0, count: nk[1]+1), count: nk[0]+1)
for i in 1..<nk[0]+1 {
    for j in 1..<nk[1]+1 {
        let (w, v) = (arr[i][0], arr[i][1])
        
        if j < w {
            d[i][j] = d[i-1][j]
        } else {
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
        }
    }
}
print(d[nk[0]][nk[1]])
