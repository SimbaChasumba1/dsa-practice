# Problem: Two Sum
# Source: LeetCode 1
# Pattern: Hash Map
# Difficulty: Easy

# Problem Statement:
# Given an array of integers nums and an integer target, return the
# indices of the two numbers that add up to target.
#
# You may assume that each input has exactly one solution, and you
# may not use the same element twice.

# Approach:
# Use a dictionary to store each number we have already seen along
# with its index. For each number, calculate the complement needed
# to reach the target. If the complement is already in the dictionary,
# return the indices of the complement and the current number.
#
# We check for the complement before adding the current number to
# the dictionary. This prevents us from accidentally using the same
# element twice.

# Alternative Approach Considered:
# Could use two nested loops to check every possible pair, which would
# take O(n²) time. The dictionary approach reduces the time to O(n)
# on average because dictionary lookups take O(1) average time.

# Time Complexity: O(n) average
# Space Complexity: O(n)

# Edge Cases Considered:
# - Duplicate numbers, such as [3, 3]
# - Negative numbers
# - Negative target
# - Solution appearing near the end of the array
# - Minimum input size of two elements
# - Numbers that do not appear in sorted order


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


# Test cases
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # expected: [0, 1]
    print(two_sum([3, 2, 4], 6))        # expected: [1, 2]
    print(two_sum([3, 3], 6))            # expected: [0, 1]
    print(two_sum([-3, 4, 3, 90], 0))   # expected: [0, 2]
