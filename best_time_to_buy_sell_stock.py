# Problem: Best Time to Buy and Sell Stock
# Source: LeetCode 121
# Pattern: Arrays / Tracking Minimum
# Difficulty: Easy

# Problem Statement:
# Given an array prices, where prices[i] represents the
# stock price on day i, return the maximum profit possible
# by buying first and selling on a later day.
#
# If no profit is possible, return 0.

# Approach:
# Track the lowest stock price seen so far.
# For each price, calculate the profit if we sold today.
# Update the maximum profit whenever we find a better result.
#
# Buying must happen before selling.

# Alternative Approach Considered:
# Checking every possible buy and sell combination would
# take O(n^2) time.
# Tracking the minimum price lets us solve the problem
# in a single pass.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Edge Cases Considered:
# - Prices always decrease
# - Prices always increase
# - Only one price
# - Empty list
# - Repeated prices
# - Maximum profit occurs at the end


def max_profit(prices):
    min_price = float("inf")
    best_profit = 0

    for price in prices:

        # Update the lowest price seen so far.
        if price < min_price:
            min_price = price

        # Calculate profit if we sell today.
        profit = price - min_price

        # Keep track of the maximum profit.
        if profit > best_profit:
            best_profit = profit

    return best_profit


# Test cases
if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # expected: 5
    print(max_profit([7, 6, 4, 3, 1]))     # expected: 0
    print(max_profit([2, 4, 1]))           # expected: 2
    print(max_profit([1, 2, 3, 4, 5]))     # expected: 4
    print(max_profit([5]))                 # expected: 0
    print(max_profit([]))                  # expected: 0