// LeetCode Problem #37 -- Sudoku Solver
// Language: C++
// Runtime: 129ms
// Memory: 10.08mb
// Date: 17 March, 2025

#include <vector>
#include <functional>

using namespace std;

void solveSudoku(vector<vector<char>>& board) {
    bool rows[9][9] = {}, cols[9][9] = {}, boxes[9][9] = {};

    // init constraints from the given board
    // this depth really sucks... oh well!
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (board[row][col] != '.') {
                int num = board[row][col] - '1';
                int boxIdx = (row / 3) * 3 + (col / 3);
                rows[row][num] = cols[col][num] = boxes[boxIdx][num] = true;
            }
        }
    }

    // solve the board with backtracking(tm)!
    // Note: this is really messy to me, it'll probably be fine
    function<bool(int, int)> solve = [&](int row, int col) {
        if (row == 9) return true;
        if (col == 9) return solve(row + 1, 0);
        if (board[row][col] != '.') return solve(row, col + 1);

        int boxIndex = (row / 3) * 3 + (col / 3);
        for (int num = 0; num < 9; num++) {
            if (!rows[row][num] && !cols[col][num] && !boxes[boxIndex][num]) {
                board[row][col] = num + '1';
                rows[row][num] = cols[col][num] = boxes[boxIndex][num] = true;

                if (solve(row, col + 1)) return true;

                // backtrack step
                board[row][col] = '.';
                rows[row][num] = cols[col][num] = boxes[boxIndex][num] = false;
            }
        }
        
        return false;
    };

    solve(0, 0);
}

// Note: Anonymous funcs are tragic.

