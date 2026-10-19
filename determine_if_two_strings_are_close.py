# Problem: Determine if Two Strings Are Close
# Source: LeetCode 1657
# Pattern: Hash Map + Frequency Counting + Sorting
# Difficulty: Medium

# Problem Statement:
# Two strings are close if you can transform one into the
# other using these operations:
# 1. Swap any two existing characters.
# 2. Transform every occurrence of one existing character
#    into another existing character, and vice versa.
#
# Return True if word1 and word2 are close. Otherwise,
# return False.
#
# Example:
# word1 = "abc"
# word2 = "bca"
# Output: True
#
# Explanation:
# The characters can be rearranged to make both strings equal.
#
# Another example:
# word1 = "a"
# word2 = "aa"
# Output: False
#
# Explanation:
# The strings have different lengths and character counts.
#
# Approach:
# First, check whether both strings have the same length.
# Then, check whether they contain the same distinct characters.
# Finally, compare their sorted character-frequency counts.
# If all checks pass, the strings are close.
#
# Alternative Approach Considered:
# Try applying every possible sequence of operations.
# This is unnecessarily complicated and inefficient.
# Comparing character sets and frequency counts is simpler.
#
# Time Complexity: O(n + k log k)
# Space Complexity: O(n + k)
# where n is the string length and k is the number of
# distinct characters.
#
# Edge Cases Considered:
# - Identical strings
# - Different string lengths
# - Different sets of characters
# - Repeated characters
# - Empty strings


def close_strings(word1, word2):
    if len(word1) != len(word2):
        return False

    counts1 = {}
    counts2 = {}

    for char in word1:
        counts1[char] = counts1.get(char, 0) + 1

    for char in word2:
        counts2[char] = counts2.get(char, 0) + 1

    if set(counts1.keys()) != set(counts2.keys()):
        return False

    return sorted(counts1.values()) == sorted(counts2.values())


# Test cases
if __name__ == "__main__":
    print(close_strings("abc", "bca"))
    # expected: True

    print(close_strings("a", "aa"))
    # expected: False

    print(close_strings("cabbba", "abbccc"))
    # expected: True

    print(close_strings("aabb", "abcc"))
    # expected: False

    print(close_strings("", ""))
    # expected: True

    print(close_strings("aab", "abb"))
    # expected: True