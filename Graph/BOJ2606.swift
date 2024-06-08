import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!
var graph: [[Int]] = Array(repeating: [], count: n+1)
var visited: [Bool] = Array(repeating: false, count: n+1)
for _ in 0..<m {
    let nm = readLine()!.split(separator: " ").map{Int($0)!}
    graph[nm[0]].append(nm[1])
    graph[nm[1]].append(nm[0])
}

var answer = 0
func dfs(_ v: Int) {
    visited[v] = true
    for i in graph[v] {
        if !visited[i] {
            answer += 1
            dfs(i)
        }
    }
}
dfs(1)
print(answer)
