import Foundation

let t = Int(readLine()!)!
var d = Array(repeating: [0,0], count: 41)
d[0] = [1,0]
d[1] = [0,1]

for i in 2..<d.count {
    d[i][0] = d[i-1][0]+d[i-2][0]
    d[i][1] = d[i-1][1]+d[i-2][1]
}

for _ in 0..<t {
    let n = Int(readLine()!)!
    print(d[n].map{String($0)}.joined(separator: " "))
}
