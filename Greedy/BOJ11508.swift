import Foundation

var N = Int(readLine()!)!
var price: [Int] = []
var sum = 0
for _ in 0..<N {
    price.append(Int(readLine()!)!)
}
price.sort(by: >)

var idx = 0
while idx < price.count {
    if idx+3 > price.count {
        sum += price[idx..<N].reduce(0,+)
        break
    }
    sum += price[idx] + price[idx+1]
    idx += 3
}

print(sum)
