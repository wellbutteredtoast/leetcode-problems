// LeetCode Problem #5 -- Longest Palindromic Substring
// Language: C++
// Runtime: 
// Memory:
// Date: 17 March, 2025

#include <string>
using namespace std;

string longestPalindrome(string s) {
    if (s.empty()) return "";

    int start = 0, maxLen = 1;
    int len = s.length();

    auto expandAroundCenter = [&](int left, int right) {
        while (left >= 0 && right < len && s[left] == s[right]) {
            left--;
            right++;
        }

        return right - left - 1; // ~ length
    };
}