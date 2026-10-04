# Problem: Longest Substring Without Repeating Characters
# Source: LeetCode 3
# Pattern: Sliding Window
# Difficulty: Medium

# Problem Statement:
# Given a string s, find the length of the longest substring without
# repeating characters.

# Approach:
# Use a sliding window with two pointers, left and right. Track the
# characters currently inside the window using a set. If a duplicate
# character is found, move the left pointer forward until the duplicate
# is removed. At each step, update the maximum window length.

# Alternative Approach Considered:
# Could use a dictionary to store the most recent index of each character
# and jump the left pointer directly past duplicates. This is also O(n),
# but the set-based sliding window is straightforward and easy to follow.

# Time Complexity: O(n)
# Space Complexity: O(min(n, k)), where k is the character set size

# Edge Cases Considered:
# - Empty string
# - Single character
# - All characters are identical
# - No duplicate characters
# - Duplicate characters appearing far apart


def length_of_longest_substring(s):
    chars = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in chars:
         chars.remove(s[left])
         left += 1
        
         
        chars.add(s[right])
        max_length = max(max_length, right - left + 1 )

    return max_length



# Test cases
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # expected: 3
    print(length_of_longest_substring("bbbbb"))     # expected: 1
    print(length_of_longest_substring("pwwkew"))    # expected: 3
    print(length_of_longest_substring(""))          # expected: 0