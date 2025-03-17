// LeetCode Problem #69 -- sqrt
// Language: C++
// Runtime: < 0ms
// Memory: 8.38mb
// Date: 17 March, 2025

int sqrt(int x) {
    if (x == 0) return 0;
    long r = x;
    while (r * r > x) {
        r = (r + x / r) / 2;
    }
    return r;
}

// Note: Good method, insanely fast, and using very little memory across a couple thousand cases.