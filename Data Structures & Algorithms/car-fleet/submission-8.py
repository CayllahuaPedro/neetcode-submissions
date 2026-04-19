class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        noOfFleets= 0
        sortedByPosition = sorted(enumerate(position), key=lambda x: x[1], reverse= True)
        carsWaiting = []
        for orgIdx, pos in sortedByPosition:
            tRemaining = (target - pos) / speed[orgIdx]
            #condition where it actually cathes up:
            if carsWaiting and carsWaiting[-1] >= tRemaining:
                continue
            else:
                noOfFleets+=1
                if carsWaiting:
                    carsWaiting.pop()
                carsWaiting.append(tRemaining)
                
        return noOfFleets;     