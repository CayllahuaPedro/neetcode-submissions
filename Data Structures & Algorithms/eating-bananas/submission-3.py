class Solution:
    def getEatingHours(self, piles: List[int], k: int) -> int:
        tiempoTotal = 0 
        for pile in piles: 
            tiempoTotal +=  math.ceil(pile /k)
        return tiempoTotal
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## el espacio de busqueda es de 1 .. maximum => luego entonces, quiero 
        ## quiero ver que mientras mas grandes sea k menos horas es no ? ya pe entonces
        left = 1
        right = max(piles)
        result = right
        while left <= right: 
            k = (left + right) // 2
            hours = self.getEatingHours(piles, k)

            if hours <= h:
                result = k 
                right = k-1
            else:
                left = k +1

        return result

        
    