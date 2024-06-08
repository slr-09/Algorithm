import Foundation

let T = Int(readLine()!)!
var graph: [[Int]] = []
for _ in 0..<T {
    let input = readLine()!.split(separator: " ").map{Int($0)!}
    graph = Array(repeating: Array(repeating: 0, count: input[0]), count: input[1])
    for _ in 0..<input[2] {
        let xy = readLine()!.split(separator: " ").map{Int($0)!}
        graph[xy[1]][xy[0]] = 1
    }
    var num = 0
    for i in 0..<input[1] {
        for j in 0..<input[0] {
            if dfs(i,j,input[0],input[1]) {
                num += 1
            }
        }
    }
    print(num)
}

func dfs(_ x: Int, _ y: Int, _ a: Int, _ b: Int) -> Bool {
    if x<0 || x>=b || y<0 || y>=a {
        return false
    }
    if graph[x][y] == 1 {
        graph[x][y] = 0
        dfs(x-1,y,a,b)
        dfs(x+1,y,a,b)
        dfs(x,y-1,a,b)
        dfs(x,y+1,a,b)
        return true
    }
    return false
}
