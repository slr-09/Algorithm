import Foundation

let nm = readLine()!.split(separator: " ").map{Int($0)!}
var visited = Array(repeating: false, count: nm[0]+1)

var answer = ""
func f(_ arr: [Int]) {
    if arr.count == nm[1] {
        answer += arr.map{String($0)}.joined(separator: " ") + "\n"
        return
    }
    
    for i in 1...nm[0] {
        if !visited[i] {
            visited[i] = true
            f(arr + [i])
            visited[i] = false
        }
    }
}

f([])
print(answer)
