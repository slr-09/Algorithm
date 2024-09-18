import Foundation

let n = Int(readLine()!)!
let length = readLine()!.split(separator: " ").map{Int($0)!}
let price = readLine()!.split(separator: " ").map{Int($0)!}

var (answer,index) = (0,0)
while index < n-1 {
    var count = 0
    for j in index..<n-1 {
        // 현재 가격보다 다음 가격이 더 크거나 같다면
        // 현재 가격 기준으로 answer에 더한다.
        if price[index] <= price[j] {
            answer += price[index]*length[j]
            count += 1
        } else {
            break
        }
    }
    index += count
}

print(answer)
