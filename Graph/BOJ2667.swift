import Foundation

func dfs(_ x: Int, _ y: Int) -> Bool {
    if x<0 || x>=n || y<0 || y>=n {
        return false
    }
    if graph[x][y] == 1 {
        num += 1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return true
    }
    return false
}

let n = Int(readLine()!)!
var graph: [[Int]] = []
for _ in 0..<n {
    graph.append(readLine()!.map{Int(String($0))!})
}

var answer = 0
var num = 0
var arr: [Int] = []
for i in 0..<n {
    for j in 0..<n {
        if dfs(i,j) {
            answer += 1
            arr.append(num)
            num = 0
        }
    }
}

print(answer)
print(arr.sorted().map{String($0)}.joined(separator: "\n"))

