#include <cctype>
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int colMaskArray[9] = {0};
        int squareMaskArray[9]= {0};
        int n = board.size(); 
        for (int i =0 ; i < n ; i++) {
            int rowMask = 0;
            for (int j=0 ; j < n ; j++) {
                if (isdigit(board[i][j])) {
                int num = board[i][j] - '0';
                    int squareNum = (i / 3) * 3 + (j/3);
                    int colMask = colMaskArray[j];
                    int squareMask = squareMaskArray[squareNum];
                        if (rowMask & (1 << num))  return false;
                        if (colMask & (1 << num)) return false;
                        if (squareMask & (1 << num )) return false;
                        squareMask = squareMask | (1 << num);
                        rowMask = rowMask | (1 << num);
                        colMask = colMask | (1 << num);
                        colMaskArray[j] = colMask;
                        squareMaskArray[squareNum] = squareMask;
                }
            }
        }
        return true;
    }
};
