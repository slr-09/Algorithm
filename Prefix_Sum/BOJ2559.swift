import Foundation

let num = readLine()!.components(separatedBy: " ").map{Int($0)!}
let arr = readLine()!.components(separatedBy: " ").map{Int($0)!}

var sum = 0
for i in 0..<num[1] {
    sum += arr[i]
}
var answer = sum
for i in 0..<num[0]-num[1] {
    answer = max(sum-arr[i]+arr[i+num[1]],answer)
    sum = sum-arr[i]+arr[i+num[1]]
}
print(answer)
