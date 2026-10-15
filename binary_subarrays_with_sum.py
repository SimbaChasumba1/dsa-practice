# Problem: Binary Subarrays With Sum
# Source: LeetCode 930
# Pattern: Prefix Sum + Hash Map
# Difficulty: Medium

# Problem Statement:
# Given a binary array nums and an integer goal,
# return the number of non-empty subarrays whose sum
# equals goal.
#
# A subarray is a contiguous part of an array.
#
# For example:
# nums = [1, 0, 1, 0, 1]
# goal = 2
# Output: 4
#
# Explanation:
# The four valid subarrays are:
# [1, 0, 1] starting at index 0
# [1, 0, 1] starting at index 2
# [1, 0, 1, 0, 1] is not valid because its sum is 3
# [0, 1, 0, 1] is valid
# [1, 0, 1, 0] is valid
#
# Another example:
# nums = [0, 0, 0, 0, 0]
# goal = 0
# Output: 15

# Approach:
# Use a running prefix sum and a hash map to track
# how often each prefix sum has appeared.
#
# Initialize prefix_sum to 0 and store its frequency
# as 1 to represent an empty prefix.
#
# Traverse the array from left to right.
#
# At each element, update the running prefix sum.
#
# A subarray has sum goal when:
# current_prefix_sum - previous_prefix_sum == goal
#
# Therefore:
# required_sum = prefix_sum - goal
#
# Add the frequency of required_sum to the total count.
#
# Record the current prefix sum in the hash map.
#
# Return the total count.

# Alternative Approach Considered:
# Use nested loops to calculate every possible subarray sum.
#
# This approach takes O(n^2) time.
#
# Prefix sums and a hash map avoid recalculating sums
# and achieve O(n) time complexity.
#
# Time Complexity: O(n), because each element is processed once.
# Space Complexity: O(n), because the hash map stores prefix sums.

# Edge Cases Considered:
# - Goal is zero
# - Array contains only zeros
# - Array contains only ones
# - Entire array sums to the goal
# - No subarray matches the goal
# - Multiple overlapping valid subarrays
# - Single-element array


def binary_subarrays_with_sum(nums, goal):
    # Store the frequency of each prefix sum.
    prefix_frequency = {0: 1}

    prefix_sum = 0
    count = 0

    for num in nums:
        # Update the running prefix sum.
        prefix_sum += num

        # Find previous prefix sums that produce
        # a subarray with the required sum.
        required_sum = prefix_sum - goal
        count += prefix_frequency.get(required_sum, 0)

        # Record the current prefix sum.
        prefix_frequency[prefix_sum] = (
            prefix_frequency.get(prefix_sum, 0) + 1
        )

    return count


# Test cases
if __name__ == "__main__":
    print(binary_subarrays_with_sum([1, 0, 1, 0, 1], 2))
    # expected: 4

    print(binary_subarrays_with_sum([0, 0, 0, 0, 0], 0))
    # expected: 15

    print(binary_subarrays_with_sum([1, 1, 1], 2))
    # expected: 2

    print(binary_subarrays_with_sum([1, 0, 0, 1], 1))
    # expected: 6

    print(binary_subarrays_with_sum([1, 1, 1], 0))
    # expected: 0

    print(binary_subarrays_with_sum([1], 1))
    # expected: 1

    print(binary_subarrays_with_sum([0], 0))
    # expected: 1

    print(binary_subarrays_with_sum([1, 1, 1, 1], 4))
    # expected: 1