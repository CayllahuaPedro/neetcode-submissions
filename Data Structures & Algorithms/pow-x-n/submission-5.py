class Solution:
    def recPow(self, x: float, n:int)-> float:
        if n==0:
            return 1;
        if n == 1:
            return x;
        abs_n=abs(n)
        b = abs_n // 2 
        pot = self.recPow(x, b)
        pot_abs= pot * pot if n % 2 == 0 else pot* pot * x
        return pot_abs if n> 0 else 1/pot_abs 
    def myPow(self, x: float, n: int) -> float:
        return self.recPow(x,n)