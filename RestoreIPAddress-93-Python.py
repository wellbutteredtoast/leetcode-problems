# LeetCode Problem #93 -- Restore IP Address
# Language: Python
# Runtime: 1ms
# Memory: 17.77mb
# Date: March 17, 2025

def restoreIpAddress(s: str) -> list[str]:
    result = []

    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append('.'.join(path))
            return
    
        if len(path) >= 4:
            return
        
        for length in range(1, 4):
            if start + length > len(s):
                break

            segment = s[start:start+length]
            if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                continue
            
            backtrack(start + length, path + [segment])
    
    backtrack(0, [])
    return result

print(restoreIpAddress("2552551135"))