class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const colMaskArray = new Array(9).fill(0)
        const squareMaskArray= new Array(9).fill(0)
        const n = board.length 
        for (let i =0 ; i < n ; i++) {
            let rowMask = 0;
            for (let j=0 ; j < n ; j++) {
                const num= parseInt(board[i][j])
                const squareNum = Math.floor(i / 3) * 3 + Math.floor(j/3)
                let colMask = colMaskArray[j];
                let squareMask = squareMaskArray[squareNum]
                if (!Number.isNaN(num)) {
                    if (rowMask & (1 << num))  return false;
                    if (colMask & (1 << num)) return false;
                    if (squareMask & (1 << num )) return false;
                    squareMask = squareMask | (1 << num)
                    rowMask = rowMask | (1 << num)
                    colMask = colMask | (1 << num)
                    colMaskArray[j] = colMask
                    squareMaskArray[squareNum] = squareMask
                }
            }
        }
        return true
    }
}

