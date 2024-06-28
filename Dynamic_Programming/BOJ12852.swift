import Foundation

var N = Int(readLine()!)!
var d = Array(repeating: 0, count: N+1)
var num: [Int] = Array(repeating: 0, count: N+1)

for i in 2..<N+1 {
    d[i] = d[i-1] + 1
    num[i] = i-1
    if i%3 == 0 && d[i] > d[i/3]+1 {
        d[i] = d[i/3]+1
        num[i] = i/3
    }
    if i%2 == 0 && d[i] > d[i/2]+1 {
        d[i] = d[i/2]+1
        num[i] = i/2
    }
}
print(d[N])
while N > 0 {
    print(N, terminator: " ")
    N = num[N]
}
