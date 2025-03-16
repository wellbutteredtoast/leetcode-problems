# LeetCode Problem #1 -- Two Sum
# Language: Python
# Runtime: 22ms
# Memory: 18.92mb
# Date: 16 March, 2025

def twoSum(nums: list[int], target: int) -> list[int]:
    # intialize an empty dictionary
    map = {}

    # enumerates over list, gets the complement, if its been found, return [i, complement]
    # if not, then put it on the list anyways
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i

    # in case nothing is found, return none
    return None