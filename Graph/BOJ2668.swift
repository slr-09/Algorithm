import Foundation

let n = Int(readLine()!)!
var graph: [Int] = [0]
for _ in 0..<n {
    graph.append(Int(readLine()!)!)
}

var (setV, setI) = (Set<Int>(), Set<Int>())
var visited: [Bool] = Array(repeating: false, count: n+1)
func dfs(_ i: Int, _ v: Int) {
    
    if visited[i] { return }
    
    // 방문
    visited[i] = true
    setI.insert(i)
    setV.insert(v)
    dfs(v, graph[v])
}

var answer = Set<Int>()
for i in 1...n {
    dfs(i, graph[i])
    
    // 두 집합 요소가 같다면
    if setV == setI {
        answer.formUnion(setI)
    }
    
    // 초기화
    setI = Set()
    setV = Set()
    visited = Array(repeating: false, count: n+1)
}

print(answer.count, Array(answer).sorted().map{String($0)}.joined(separator: "\n"), separator: "\n")
