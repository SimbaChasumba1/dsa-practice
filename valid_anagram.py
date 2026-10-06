# Problem: Valid Anagram
# Source: LeetCode 242
# Pattern: Hash Map / Frequency Counting
# Difficulty: Easy

# Problem Statement:
# Given two strings s and t, return True if t is an anagram of s.
# An anagram is a word or phrase formed by rearranging the letters
# of another word or phrase using all the original letters exactly once.
#
# For example:
# "anagram" and "nagaram" are anagrams.
# "rat" and "car" are not anagrams.

# Approach:
# Use a dictionary to count how many times each character appears
# in the first string. Then go through the second string and reduce
# the corresponding character count.
#
# If a character does not exist in the dictionary, or its count becomes
# negative, the strings cannot be anagrams.
#
# If the strings have the same length and all character counts match,
# then they are anagrams.

# Alternative Approach Considered:
# Could sort both strings and compare the sorted results. This would
# take O(n log n) time because of sorting. A frequency-counting
# dictionary gives us O(n) time, so it is more efficient.

# Time Complexity: O(n)
# Space Complexity: O(1), because the input only contains lowercase
# English letters (at most 26 different characters)

# Edge Cases Considered:
# - Strings with different lengths
# - Single-character strings
# - Empty strings
# - Repeated characters
# - Completely different characters
# - Strings containing the same characters in a different order


def is_anagram(s, t):
    # If the strings have different lengths, they cannot contain
    # exactly the same characters.
    if len(s) != len(t):
        return False

    counts = {}

    # Count each character in the first string.
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Subtract each character found in the second string.
    for char in t:
        if char not in counts:
            return False

        counts[char] -= 1

        # More occurrences in t than in s means they are not anagrams.
        if counts[char] < 0:
            return False

    return True


# Test cases
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # expected: True
    print(is_anagram("rat", "car"))          # expected: False
    print(is_anagram("a", "a"))              # expected: True
    print(is_anagram("a", "b"))              # expected: False
    print(is_anagram("", ""))                # expected: True
