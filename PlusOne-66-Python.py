# LeetCode Problem #66 -- Plus One
# Language: Python
# Runtime: < 0ms
# Memory: 17.72mb
# Date: 17 March, 2025

def plusOne(digits: list[int]) -> list[int]:
    digits_str = ""

    # This is terrible.
    for k in range(len(digits)):
        digits_str += str(digits[k])

    plusone_result = str(int(digits_str) + 1)
    plusonefinallist = []

    # I love loops
    for j in range(len(plusone_result)):
        plusonefinallist.append(int(plusone_result[j]))

    return plusonefinallist
    # the pain
