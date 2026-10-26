class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = 1e9
        for price in prices:
            if price>buy:
                ans = max(ans,price-buy)
            elif price<buy:
                buy = price
        return ans
        