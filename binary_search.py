# Problem: Binary Search
# Source: LeetCode 704
# Pattern: Binary Search
# Difficulty: Easy

# Problem Statement:
# Given a sorted list of distinct integers nums and an integer target,
# return the index of target if it exists in nums.
# Otherwise, return -1.
#
# For example:
# nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
#
# nums = [-1, 0, 3, 5, 9, 12], target = 2
# Output: -1

# Approach:
# Use two pointers: left and right.
# They represent the current search range.
#
# Calculate the middle index of the range.
#
# If nums[mid] equals target, return mid.
#
# If nums[mid] is smaller than target, search the right half.
#
# If nums[mid] is greater than target, search the left half.
#
# Continue until the target is found or the search range is empty.

# Alternative Approach Considered:
# Could use a linear search and check every element.
# This takes O(n) time in the worst case.
#
# Binary search eliminates half of the remaining search range
# at each step, making it O(log n).
#
# The input must be sorted for binary search to work correctly.

# Time Complexity: O(log n)
# Space Complexity: O(1), because we only use a few variables.

# Edge Cases Considered:
# - Empty list
# - Single-element list
# - Target is the first element
# - Target is the last element
# - Target is not present
# - Target is smaller than every element
# - Target is larger than every element


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    # Continue while the search range is not empty.
    while left <= right:

        # Find the middle index without adding left and right directly.
        mid = left + (right - left) // 2

        # Target found.
        if nums[mid] == target:
            return mid

        # Target must be in the right half.
        elif nums[mid] < target:
            left = mid + 1

        # Target must be in the left half.
        else:
            right = mid - 1

    # Target was not found.
    return -1


# Test cases
if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))
    # expected: 4

    print(binary_search([-1, 0, 3, 5, 9, 12], 2))
    # expected: -1

    print(binary_search([5], 5))
    # expected: 0

    print(binary_search([5], 2))
    # expected: -1

    print(binary_search([], 7))
    # expected: -1

    print(binary_search([1, 3, 5, 7, 9], 1))
    # expected: 0

    print(binary_search([1, 3, 5, 7, 9], 9))
    # expected: 4