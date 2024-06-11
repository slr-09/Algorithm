import Foundation

let nm = readLine()!.split(separator: " ").map{Int($0)!}
var graph: [[Int]] = Array(repeating: [], count: nm[0]+1)
for _ in 0..<nm[1] {
    let ab = readLine()!.split(separator: " ").map{Int($0)!}
    graph[ab[0]].append(ab[1])
    graph[ab[1]].append(ab[0])
}


var visited: [Bool] = Array(repeating: false, count: nm[0]+1)
func dfs(_ v: Int) {
    visited[v] = true
    
    for i in graph[v] {
        if !visited[i] {
            dfs(i)
        }
    }
}

var answer = 0
for i in 1..<graph.count {
    if !visited[i] {
        dfs(i)
        answer += 1
    }
}
print(answer)
