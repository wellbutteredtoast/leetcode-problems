# LeetCode Problem #50 -- Power
# Language: Python
# Runtime: ~0ms (??)
# Memory: 17.71mb
# Date: 17 March, 2025

def power(x: float, n: int) -> float:
    # x -> coefficient
    # n -> power

    if x == 0: return 0.0

    return float(x**n)

# Note: I have no idea how the runtime is under 1ms.
#       I won't complain, it's the fastest on LeetCode.
