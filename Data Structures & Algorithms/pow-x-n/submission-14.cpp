class Solution {
public:
    double myPow(double x, int n) {
        long long abs_n = n;
        if (abs_n < 0){
            abs_n = -abs_n;
        }
        double res = 1.0;
        while (abs_n > 0){
            if (abs_n & 1) {
                res = res * x;
            }
            x = x* x;
            abs_n >>= 1;
        }
        if (n < 0){
            return 1/res;
        }
        else{
            return res;
        }
    }
};
