let nm = readLine()!.split(separator: " ").map { Int($0)! }
var graph: [[Int]] = Array(repeating: [], count: nm[0]+1)
var visited = Array(repeating: false, count: graph.count)
var visited2 = Array(repeating: false, count: graph.count)

for _ in 0..<nm[1] {
    let v = readLine()!.split(separator: " ").map{Int($0)!}
    graph[v[0]].append(v[1])
    graph[v[1]].append(v[0])
}
let sortedGraph = graph.map{ $0.sorted() }

func dfs(v: Int) {
    visited[v] = true
    print(v, terminator: " ")
    
    for i in sortedGraph[v] {
        if !visited[i] {
            dfs(v: i)
        }
    }
}

func bfs(v: Int) {
    var queue = [v]
    visited2[v] = true
    
    // 큐가 빌 때까지 반복
    while !queue.isEmpty {
        let s = queue.removeFirst()
        print(s, terminator: " ")
        
        for i in sortedGraph[s] {
            if !visited2[i] {
                queue.append(i)
                visited2[i] = true
            }
        }
    }
}

dfs(v: nm[2])
print()
bfs(v: nm[2])
