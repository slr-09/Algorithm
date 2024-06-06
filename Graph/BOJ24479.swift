import Foundation

let nm = readLine()!.split(separator: " ").map{ Int($0)! }
var graph = Array(repeating: [Int](), count: nm[0]+1)
for _ in 0..<nm[1] {
    let uv = readLine()!.split(separator: " ").map{Int($0)!}
    graph[uv[0]].append(uv[1])
    graph[uv[1]].append(uv[0])
}
for i in 0..<graph.count {
    graph[i].sort(by: <)
}

var answer = Array(repeating: 0, count: nm[0]+1)
var turn = 1
func dfs(v: Int) {
    answer[v] = turn
    
    for i in graph[v] {
        if answer[i] == 0 {
            turn += 1
            dfs(v: i)
        }
    }
}

dfs(v: nm[2])
for i in 1..<answer.count {
    print(answer[i])
}
