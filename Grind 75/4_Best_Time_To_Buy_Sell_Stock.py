'''
Approach
Initialize variables buy with the first element of the prices array and profit as 0.
Iterate through the prices starting from the second element.
Update the buy variable if the current price is lower than the current buying price.
Update the profit if the difference between the current price and the buying price is 
greater than the current profit.
Return the final profit.
Kadane's Algorithm
Kadane's Algorithm is a dynamic programming technique used to find the maximum subarray 
sum in an array of numbers. The algorithm maintains two variables: max_current represents 
the maximum sum ending at the current position, and max_global represents the maximum 
subarray sum encountered so far. At each iteration, it updates max_current to include the 
current element or start a new subarray if the current element is larger than the accumulated sum. 
The max_global is updated if max_current surpasses its value.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
        