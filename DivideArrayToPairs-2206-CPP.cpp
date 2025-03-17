// LeetCode Problem #2206 -- Divide Array Into Equal Pairs
// Language: C++
// Runtime: < 0ms
// Memory: 18.28mb
// Date: 17 March, 2025

#include <vector>
#include <unordered_map>

bool divideArray(std::vector<int>& nums) {
    std::unordered_map<int, int> freq;

    // Count the frequency of each occuring number
    for (int num : nums) {
        freq[num]++;
    }

    // Check if all known counts are even (this is important)
    for (const auto& [key, count] : freq) {
        if (count % 2 != 0) {
            return false;
        }
    }
    
    return true;
}