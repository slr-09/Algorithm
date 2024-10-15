import Foundation

let n = Int(readLine()!)!
var d: [[Int]] = Array(repeating: [0,0], count: n)
var arr: [Int] = []
for _ in 0..<n {
    arr.append(Int(readLine()!)!)
}

d[0][1] = arr[0]

// d의 각 요소는 [0,0] 형태
// 0번 인덱스는 바로 직전 계단을 밟고 오는 경우, 1번 인덱스는 바로 직전 계단을 밟지 않는 경우 (전전 계단을 밟은 경우)
if n > 1 {
    d[1] = [arr[0]+arr[1], arr[1]]
    for i in 2..<n {
        let current = arr[i]
        d[i] = [d[i-1][1] + current, d[i-2].max()! + current]
    }
}
print(d[n-1].max()!)
