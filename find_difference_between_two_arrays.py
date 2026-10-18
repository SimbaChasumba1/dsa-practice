# Problem: Find the Difference Between Two Arrays
# Source: LeetCode 2215
# Pattern: Hash Set / Set Difference
# Difficulty: Easy

# Problem Statement:
# Given two integer arrays nums1 and nums2, return a list
# containing two lists:
# - The distinct numbers in nums1 that are not in nums2.
# - The distinct numbers in nums2 that are not in nums1.
#
# Example:
# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
# Output: [[1, 3], [4, 6]]
#
# Explanation:
# 1 and 3 only appear in nums1.
# 4 and 6 only appear in nums2.
#
# Approach:
# Convert both arrays into sets to remove duplicates.
# Use set difference to find the elements that appear
# exclusively in each set.
# Convert the results back into lists.
#
# Alternative Approach Considered:
# Check every element against the other array using loops.
# This can take O(n * m) time.
# Sets provide a more efficient average-case solution.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Edge Cases Considered:
# - Both arrays are empty
# - Both arrays contain the same numbers
# - One array is empty
# - Arrays contain duplicate values
# - Arrays contain negative numbers


def find_difference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    only_in_nums1 = list(set1 - set2)
    only_in_nums2 = list(set2 - set1)

    return [only_in_nums1, only_in_nums2]


# Test cases
if __name__ == "__main__":
    print(find_difference([1, 2, 3], [2, 4, 6]))
    # expected: [[1, 3], [4, 6]] (order may vary)

    print(find_difference([1, 2, 3], [1, 2, 3]))
    # expected: [[], []]

    print(find_difference([], [1, 2]))
    # expected: [[], [1, 2]] (order may vary)

    print(find_difference([1, 1, 2], [2, 2, 3]))
    # expected: [[1], [3]]

    print(find_difference([-1, -2, 0], [-2, 1]))
    # expected: [[-1, 0], [1]] (order may vary)