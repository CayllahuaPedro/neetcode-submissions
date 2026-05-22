impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut abs_n = n as i64;
        if abs_n < 0 {
            abs_n = -abs_n;
        }
        let mut res = 1.0;
        let mut base = x;
        while abs_n > 0 {
            if (abs_n & 1) ==1 {
                res = res * base;
            }
            base = base*base;
            abs_n >>=1;
        }
        if n<0 {
            1.0/res
        }
        else{
            res
        }
    }
}
