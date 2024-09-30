import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
var (n,d,k,c) = (input[0], input[1], input[2], input[3])
var arr: [Int] = []
for _ in 0..<n {
    arr.append(Int(readLine()!)!)
}

// 쿠폰 번호 미리 넣어놓기
var dict: Dictionary<Int, Int> = [c: 1]
var (st, ed) = (0, k-1)

// 0부터 k개
for i in st...ed {
    dict[arr[i], default: 0] += 1
}

var answer = dict.count
while st < n-1 {
    // 시작점 이동
    dict[arr[st]]! -= 1
    if dict[arr[st]]! == 0 {
        dict.removeValue(forKey: arr[st])
    }
    st += 1
    
    // 끝점 이동
    ed += 1
    // 배열의 첫 인덱스로 이동
    if ed >= n {
        ed -= n
    }
    dict[arr[ed], default: 0] += 1
    
    answer = max(answer, dict.count)
}

print(answer)
