# Problem: Unique Number of Occurrences
# Source: LeetCode 1207
# Pattern: Hash Map + Hash Set
# Difficulty: Easy

# Problem Statement:
# Given an array of integers arr, return True if the number
# of occurrences of each value is unique. Otherwise, return False.
#
# Example:
# arr = [1, 2, 2, 1, 1, 3]
# Output: True
#
# Explanation:
# 1 occurs 3 times, 2 occurs 2 times, and 3 occurs once.
# Every occurrence count is unique.
#
# Another example:
# arr = [1, 2]
# Output: False
#
# Explanation:
# Both numbers occur once, so their counts are not unique.
#
# Approach:
# Count the occurrences of every number using a dictionary.
# Store the occurrence counts in a list.
# Convert the list into a set to remove duplicate counts.
# If both collections have the same length, all counts
# were unique.
#
# Alternative Approach Considered:
# Compare every pair of occurrence counts.
# This takes O(n^2) time in the worst case.
# Using a set provides a more efficient solution.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Edge Cases Considered:
# - One distinct number
# - Every number appears once
# - Two numbers have equal occurrence counts
# - Negative numbers
# - Multiple repeated numbers


def unique_occurrences(arr):
    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    frequencies = list(counts.values())

    return len(frequencies) == len(set(frequencies))


# Test cases
if __name__ == "__main__":
    print(unique_occurrences([1, 2, 2, 1, 1, 3]))
    # expected: True

    print(unique_occurrences([1, 2]))
    # expected: False

    print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1,
                              -3, 10, 0]))
    # expected: True

    print(unique_occurrences([5]))
    # expected: True

    print(unique_occurrences([1, 1, 2, 2]))
    # expected: False

    print(unique_occurrences([1, 1, 1, 2, 2, 3]))
    # expected: True