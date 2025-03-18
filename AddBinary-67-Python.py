# LeetCode Problem #67 -- Add Binary
# Language: Python
# Runtime: < 0ms
# Memory: 17.86mb
# Date: 17 March, 2025

def addBinary(a: str, b: str) -> str:

    # It can be assumed that there is no leading '0' in a or b
    # len(a) >= 1 && len(b) <= 10^4

    res = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        # Check if i/j are in range
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        # Sum up, append (total mod 2) to the res
        total = bit_a + bit_b + carry
        res.append(str(total % 2))

        # Check carry biy, then move to the next bit
        carry = total // 2
        i, j = i - 1, j - 1
    
    return ''.join(res[::-1])
    # This is the weirdest return statement I've ever made
    # But hey it works and honestly I'm tired of binary lol