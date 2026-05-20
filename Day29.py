# Day 29 - Best-time-to-buy-and-sell-stocK
# Platform: LeetCode

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')   # Track the lowest price seen so far
        max_profit = 0             # Track the maximum profit possible
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit


# Quick test cases 
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) 
    print(s.maxProfit([7,6,4,3,1]))  
