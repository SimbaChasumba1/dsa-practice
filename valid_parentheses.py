# Problem: Valid Parentheses
# Source: LeetCode 20
# Pattern: Stack
# Difficulty: Easy

# Problem Statement:
# Given a string s containing only the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# A string is valid if:
# 1. Every opening bracket is closed by the same type of bracket.
# 2. Opening brackets are closed in the correct order.
# 3. Every closing bracket has a corresponding opening bracket.
#
# For example:
# s = "()"
# Output: True
#
# s = "()[]{}"
# Output: True
#
# s = "(]"
# Output: False
#
# s = "([)]"
# Output: False
#
# s = "{[]}"
# Output: True

# Approach:
# Use a stack to keep track of opening brackets.
#
# Create a dictionary mapping each closing bracket
# to its corresponding opening bracket.
#
# Loop through every character in the string.
#
# If the character is an opening bracket,
# push it onto the stack.
#
# If the character is a closing bracket:
# - Check whether the stack is empty.
# - Check whether the top opening bracket matches it.
# - If either condition fails, return False.
# - Otherwise, remove the opening bracket from the stack.
#
# After processing the entire string, return True
# only if the stack is empty.
#
# Alternative Approach Considered:
# Could repeatedly search for matching bracket pairs
# and remove them from the string.
#
# However, repeatedly modifying the string can be inefficient.
#
# A stack processes each character once, making it O(n).
#
# Time Complexity: O(n), because each character is processed once.
# Space Complexity: O(n), because the stack can store up to n characters.
#
# Edge Cases Considered:
# - Empty string
# - Single opening bracket
# - Single closing bracket
# - Matching brackets
# - Mismatched bracket types
# - Incorrect bracket ordering
# - Nested brackets
# - Multiple consecutive bracket pairs


def is_valid(s):
    # Map each closing bracket to its matching opening bracket.
    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # Store opening brackets until their matching closing brackets appear.
    stack = []

    for char in s:

        # Opening bracket: add it to the stack.
        if char in "({[":
            stack.append(char)

        # Closing bracket: check whether it matches the most recent opening.
        else:
            # No opening bracket is available to match.
            if not stack:
                return False

            # The most recent opening bracket must match this closing bracket.
            if stack[-1] != brackets[char]:
                return False

            # Remove the matched opening bracket.
            stack.pop()

    # All brackets must have been matched.
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    print(is_valid("()"))
    # expected: True

    print(is_valid("()[]{}"))
    # expected: True

    print(is_valid("(]"))
    # expected: False

    print(is_valid("([)]"))
    # expected: False

    print(is_valid("{[]}"))
    # expected: True

    print(is_valid(""))
    # expected: True

    print(is_valid("("))
    # expected: False

    print(is_valid("]"))
    # expected: False

    print(is_valid("((()))"))
    # expected: True

    print(is_valid("[{()}]"))
    # expected: True