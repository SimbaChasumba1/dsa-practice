# Problem: Product of Array Except Self
# Source: LeetCode 238
# Pattern: Prefix and Suffix Products
# Difficulty: Medium

# Problem Statement:
# Given an integer array nums, return an array answer
# such that answer[i] is equal to the product of all
# elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is
# guaranteed to fit in a 32-bit integer.
#
# You must solve the problem without using division
# and in O(n) time complexity.
#
# For example:
# nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
#
# Explanation:
# answer[0] = 2 * 3 * 4 = 24
# answer[1] = 1 * 3 * 4 = 12
# answer[2] = 1 * 2 * 4 = 8
# answer[3] = 1 * 2 * 3 = 6
#
# nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

# Approach:
# Use prefix and suffix products.
#
# First, create an answer array filled with 1s.
#
# Traverse the array from left to right.
#
# Store the product of all elements to the left
# of each index in answer[i].
#
# Maintain a prefix_product variable to track
# the product of elements seen so far.
#
# Next, traverse the array from right to left.
#
# Multiply answer[i] by the product of all elements
# to the right of the current index.
#
# Maintain a suffix_product variable to track
# the product of elements seen from the right.
#
# Return the answer array.

# Alternative Approach Considered:
# Could calculate the total product and divide it
# by each element.
#
# However, division is not allowed by the problem.
# It also fails when the array contains zero.
#
# Prefix and suffix products avoid division and
# process the array in linear time.
#
# Time Complexity: O(n), because the array is traversed twice.
# Space Complexity: O(1) auxiliary space, excluding the
# output array, as required by the problem.

# Edge Cases Considered:
# - Two elements
# - Multiple zeros
# - Exactly one zero
# - Negative numbers
# - All positive numbers
# - Array containing ones
# - Products involving negative numbers


def product_except_self(nums):
    n = len(nums)

    # Initialize the answer array with 1s.
    answer = [1] * n

    # Track the product of all elements to the left.
    prefix_product = 1

    for i in range(n):
        answer[i] = prefix_product
        prefix_product *= nums[i]

    # Track the product of all elements to the right.
    suffix_product = 1

    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]

    return answer


# Test cases
if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))
    # expected: [24, 12, 8, 6]

    print(product_except_self([-1, 1, 0, -3, 3]))
    # expected: [0, 0, 9, 0, 0]

    print(product_except_self([2, 3]))
    # expected: [3, 2]

    print(product_except_self([0, 0]))
    # expected: [0, 0]

    print(product_except_self([1, 1, 1, 1]))
    # expected: [1, 1, 1, 1]

    print(product_except_self([-1, -2, -3, -4]))
    # expected: [-24, -12, -8, -6]

    print(product_except_self([1, 2, 0, 4]))
    # expected: [0, 0, 8, 0]

    print(product_except_self([5, 0, 2]))
    # expected: [0, 10, 0]