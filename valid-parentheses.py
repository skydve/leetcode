# Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s):
    m = {')':'(', '}':'{', ']':'['}
    stack = []
    for char in s:
        if char in m.values():
            stack.append(char)
        else:
            if stack == [] or m[char] != stack.pop():
                return False
    return stack == []




