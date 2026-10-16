# Problem: Contiguous Array
# Source: LeetCode 525
# Pattern: Prefix Sum + Hash Map
# Difficulty: Medium

# Problem Statement:
# Given a binary array nums, return the maximum length
# of a contiguous subarray with an equal number of 0s and 1s.
#
# For example:
# nums = [0, 1]
# Output: 2
#
# Explanation:
# The entire array contains one 0 and one 1.
#
# Another example:
# nums = [0, 1, 0]
# Output: 2
#
# Explanation:
# The subarray [0, 1] or [1, 0] contains an equal
# number of 0s and 1s.
#
# Another example:
# nums = [0, 1, 1, 0, 1, 1, 1, 0]
# Output: 4
#
# Explanation:
# The longest valid subarray is [1, 1, 0, 1, 1, 1, 0]
# is not balanced; one valid maximum-length subarray
# is [1, 1, 0, 1, 1, 1, 0] only if counts match.
# A correct longest balanced subarray is [0, 1, 1, 0],
# which has length 4.

# Approach:
# Replace every 0 with -1 and keep every 1 as 1.
#
# A subarray has an equal number of 0s and 1s when
# its transformed sum equals 0.
#
# Use a running prefix sum to track the transformed sum.
#
# Store the earliest index where each prefix sum appears.
#
# If the same prefix sum appears again, the subarray
# between those two indices has sum 0.
#
# Calculate its length and update the maximum length.
#
# Initialize the map with {0: -1} to handle a valid
# subarray that starts at index 0.
#
# Return the maximum length.

# Alternative Approach Considered:
# Check every possible subarray and count its zeros and ones.
#
# This approach takes O(n^2) time or more, depending
# on how the counts are calculated.
#
# Prefix sums and a hash map solve the problem in O(n) time.

# Time Complexity: O(n), because each element is processed once.
# Space Complexity: O(n), because the hash map stores prefix sums.

# Edge Cases Considered:
# - Array contains only zeros
# - Array contains only ones
# - Array has equal numbers of zeros and ones
# - Longest valid subarray starts at index 0
# - Longest valid subarray ends at the last index
# - Multiple subarrays have the same maximum length
# - Single-element array


def find_max_length(nums):
    # Store the earliest index of each prefix sum.
    first_occurrence = {0: -1}

    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        # Treat 0 as -1 and 1 as 1.
        if num == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        # If the prefix sum has appeared before,
        # the elements between the indices sum to zero.
        if prefix_sum in first_occurrence:
            length = i - first_occurrence[prefix_sum]
            max_length = max(max_length, length)
        else:
            # Keep the earliest occurrence to maximize length.
            first_occurrence[prefix_sum] = i

    return max_length


# Test cases
if __name__ == "__main__":
    print(find_max_length([0, 1]))
    # expected: 2

    print(find_max_length([0, 1, 0]))
    # expected: 2

    print(find_max_length([0, 0, 1, 1]))
    # expected: 4

    print(find_max_length([0, 0, 0]))
    # expected: 0

    print(find_max_length([1, 1, 1]))
    # expected: 0

    print(find_max_length([0, 1, 1, 0, 1, 0]))
    # expected: 6

    print(find_max_length([1]))
    # expected: 0

    print(find_max_length([0, 1, 0, 1, 0, 1]))
    # expected: 6