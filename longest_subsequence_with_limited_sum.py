# Problem: Longest Subsequence With Limited Sum
# Source: LeetCode 2389
# Pattern: Sorting / Prefix Sum / Binary Search
# Difficulty: Easy

# Problem Statement:
# Given an integer array nums and an integer array queries,
# return an answer for each query.
#
# Each answer should be the maximum size of a subsequence
# of nums whose sum is less than or equal to the query value.
#
# Example:
# nums = [4, 5, 2, 1]
# queries = [3, 10, 21]
# Output: [2, 3, 4]
#
# Explanation:
# Query 3: [1, 2] has a sum of 3, so the answer is 2.
# Query 10: [1, 2, 4] has a sum of 7, so the answer is 3.
# Query 21: [1, 2, 4, 5] has a sum of 12, so the answer is 4.
#
# Approach:
# First, sort nums in ascending order.
# This allows us to choose the smallest numbers first,
# maximizing the number of elements within each query limit.
#
# Next, calculate the prefix sum of the sorted array.
# Each prefix sum represents the total of all elements
# from the beginning of the array up to that position.
#
# Use binary search with bisect_right to find the
# largest prefix sum that does not exceed each query.
#
# The resulting position represents the maximum number
# of elements that can fit within the query limit.
#
# Alternative Approach Considered:
# Sort the array and use a loop for each query.
# Keep adding elements until the sum exceeds the query.
#
# This approach works but can take O(n * q) time,
# where n is the length of nums and q is the number
# of queries.
#
# Binary search improves the efficiency of each query.
#
# Time Complexity: O(n log n + q log n)
# Space Complexity: O(n)
#
# Edge Cases Considered:
# - Empty nums array
# - Empty queries array
# - A query smaller than every element
# - A query larger than the sum of all elements
# - Duplicate numbers in nums
# - A nums array containing one element
# - Multiple queries with the same value


from bisect import bisect_right


def answer_queries(nums, queries):
    nums.sort()

    prefix_sum = []
    total = 0

    for num in nums:
        total += num
        prefix_sum.append(total)

    result = []

    for query in queries:
        count = bisect_right(prefix_sum, query)
        result.append(count)

    return result


# Test cases
if __name__ == "__main__":

    print(answer_queries([4, 5, 2, 1], [3, 10, 21]))
    # expected: [2, 3, 4]

    print(answer_queries([2, 3, 4, 5], [1]))
    # expected: [0]

    print(answer_queries([1, 2, 3], [6]))
    # expected: [3]

    print(answer_queries([5], [4, 5, 6]))
    # expected: [0, 1, 1]

    print(answer_queries([1, 1, 2, 2], [2, 3, 6]))
    # expected: [2, 3, 4]

    print(answer_queries([], [1, 2, 3]))
    # expected: [0, 0, 0]

    print(answer_queries([1, 2, 3], []))
    # expected: []

    print(answer_queries([3, 3, 3], [3, 6, 9]))
    # expected: [1, 2, 3]
