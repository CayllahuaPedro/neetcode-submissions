class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)
        res = 1.0
        while abs_n > 0:
            if abs_n % 2 != 0:
                res *= x
            x*=x
            abs_n //= 2
        return res if n > 0 else 1.0/res