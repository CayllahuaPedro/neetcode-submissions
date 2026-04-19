class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const colsSets = Array.from({length:9}, () => new Set())
        const squareSets= Array.from({length:9}, () => new Set())
        const n = board.length 
        for (let i =0 ; i < n ; i++) {
            const rowSet = new Set();
            for (let j=0 ; j < n ; j++) {
                const num= parseInt(board[i][j])
                const squareNum = Math.floor(i / 3) * 3 + Math.floor(j/3)
                const colSet = colsSets[j];
                const squareSet = squareSets[squareNum]
                if (!Number.isNaN(num)) {
                    if (rowSet.has(num)) return false;
                    if (colSet.has(num)) return false;
                    if (squareSet.has(num)) return false;
                    colSet.add(num);
                    rowSet.add(num)
                    squareSet.add(num)
                }
            }
        }
        return true
    }
}
