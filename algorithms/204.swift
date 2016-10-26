// https://leetcode.com/problems/count-primes

class Solution {
    func countPrimes(n: Int) -> Int {
        guard n > 2 else { return 0 }
        var isPrime = [Bool](count: n, repeatedValue: true)
        isPrime[0..<2] = [false, false]
        for i in 0..<Int(sqrt(Double(n)))+1 {
            if isPrime[i] {
                (i*i).stride(to: n, by: i).map { isPrime[$0] = false }
            }
        }
        return isPrime.filter { $0 == true }.count
    }
}
