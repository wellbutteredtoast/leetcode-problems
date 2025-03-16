# LeetCode Problem #9 -- Palindrome Number
# Language: Python
# Runtime: 7ms
# Memory: 17.70mb
# Date: 16 March, 2025

def isPalindrome(x: int) -> bool:
    string_x = str(x)
    rev_string = string_x[::-1]

    if string_x == rev_string:
        return True
    else:
        return False
    
# Note: There is almost guarenteed to be a superior solution which does not involve strings.
#       Since strings are pretty heavy on the Python runtime. I'll come back to this later
#       to make a more memory efficient solution.