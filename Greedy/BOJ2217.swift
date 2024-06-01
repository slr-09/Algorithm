var n = Int(readLine()!)!
var arr: [Int] = []
for _ in 0..<n {
    arr.append(Int(readLine()!)!)
}
arr.sort()
var answer = 0
for i in arr {
    answer = max(answer, i*n)
    n -= 1
}
print(answer)
