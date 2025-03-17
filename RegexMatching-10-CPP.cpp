// LeetCode Problem #10 -- Regex Matching
// Language: C++
// Runtime: 3ms
// Memory: 8.94mb
// Date: 17 March, 2025

#include <vector>
#include <string>

using namespace std;

bool isMatch(string s, string p) {
    int m = s.size(), n = p.size();
    vector<vector<bool>> dp(m + 1, vector<bool>(n+1, false));

    dp[0][0] = true;

    // Handle '*' patterns
    for (int j = 1; j <= n; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 2]; // Removes the '*'
        }
    }

    // Fill DP table
    // Note: This is awful and I want it to burn
    //       Please do not ever do this...
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 2];
                // '*' as zero occurrence of preceding element
                if (p[j - 2] == s[i - 1] || p[j - 2] == '.') {
                    dp[i][j] = dp[i][j] || dp[i - 1][j];
                    // '*' as one or more occurrence
                }
            }
        }
    }

    // This is fantastic, I never want to do this again...
    // The hardest thing I've ever done to date D:
    return dp[m][n];
}