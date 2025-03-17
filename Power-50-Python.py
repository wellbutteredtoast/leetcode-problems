# LeetCode Problem #50 -- Power
# Language: Python
# Runtime: < 0ms
# Memory: 17.71mb
# Date: 17 March, 2025

def power(x: float, n: int) -> float:
    # x -> coefficient
    # n -> power

    if x == 0: return 0.0

    return float(x**n)