# LeetCode Problem #7 -- Reverse Integer
# Language: Python
# Runtime: 49ms
# Memory: 17.77mb
# Date: 16 March, 2025

def reverse(self, x: int) -> int:
    X_UPPER_BOUNDS = 2147483647
    X_LOWER_BOUNDS = -2147483648

    if not isinstance(x, int):
        return None

    string_x = str(x)
    if x < 0:
        reversed_x = '-' + string_x[:0:-1]
    else:
        reversed_x = string_x[::-1]

    reversed_int = int(reversed_x)

    if reversed_int > X_UPPER_BOUNDS or reversed_int < X_LOWER_BOUNDS:
        return 0

    return reversed_int

# Note: The runtime isn't amazing, but hey that's over 1060 test cases.
#       A fine solution for small batches like this but probably not
#       the best move for 10s of thousands of cases.
#
#       I may return to this later to improve this.