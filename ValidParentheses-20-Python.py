# LeetCode Problem #20 -- Two Sum
# Language: Python
# Runtime: 3ms
# Memory: 17.77mb
# Date: 17 March, 2025

def isValid(s: str) -> bool:
    stack = []
    mapping = {")":"(", "]":"[", "}":"{"}

    for symbol in s:
        # If left, push to stack
        if symbol in mapping.values():
            stack.append(symbol)
        # If right, check if it matches stack
        elif symbol in mapping.keys():
            if stack and stack[-1] == mapping[symbol]:
                stack.pop()
            else:
                return False
            
    # If the stack is empty, everything was matched, yippee!
    return not stack

# Note: Not the most elegant looking solution but that runtime is to die for.
#       Python is dense when stacked like this but it works and that's important!