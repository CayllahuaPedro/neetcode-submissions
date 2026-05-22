class Solution {
    /**
     * @param {number} x
     * @param {number} n
     * @return {number}
     */
    myPow(x: number, n: number): number {
        let abs_n= Math.abs(n)
        let res = 1
        while (abs_n > 0) {
            if (abs_n & 1) {
                res *= x;
            }
            x*=x
            abs_n >>=1
        }
        return n < 0 ? 1/res : res
    }
}
