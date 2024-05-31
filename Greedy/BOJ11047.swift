let nk = readLine()!.split(separator: " ").map { Int($0)! }
var arr: [Int] = []
for _ in 0..<nk[0] {
    arr.append(Int(readLine()!)!)
}
var money = nk[1]
var answer = 0
for i in 0..<nk[0] {
    let coin = arr[nk[0]-1-i]
    if money >= coin {
        answer += money/coin
        money %= coin
    }
}
print(answer)
