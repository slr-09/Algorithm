import Foundation

let p = Int(readLine()!)!
for _ in 0..<p {
    var tcase = readLine()!.split(separator: " ").map{Int($0)!}
    var answer = [tcase[0], 0]
    for i in 2...20 {
        // 순서를 바꿀 학생
        let ch = tcase[i]
        
        // 본인보다 앞에 있는 학생을 비교하며
        for j in 1..<i {
            // 본인 키보다 크다면
            if ch < tcase[j] {
                // 순서 재배치
                tcase.remove(at: i)
                tcase.insert(ch, at: j)
                // 물러난 걸음 수
                answer[1] += i-j
                break
            }
        }
    }
    print(answer.map{String($0)}.joined(separator: " "))
}
