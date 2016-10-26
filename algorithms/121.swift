// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution {
    func maxProfit(prices: [Int]) -> Int {
        var minPrice = Int.max
        var maxProfit = 0
        for p in prices {
            minPrice = min(p, minPrice)
            maxProfit = max(p-minPrice, maxProfit)
        }
        return maxProfit
    }
}
