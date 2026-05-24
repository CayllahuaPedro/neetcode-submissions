from collections import defaultdict
class Solution:
    def UpdateMap(self, countFreq: dict[str, int], elem: str):
        if countFreq[elem] == 0:
            countFreq.pop(elem)
        else:
            countFreq[elem] -= 1 
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        countFreq1 = defaultdict(int)
        for char in s1:
            countFreq1[char] +=1
        left = 0
        countFreq2 = defaultdict(int)
        for right in range (len(s2)):
            print("right: ", right)
            if s2[right] not in countFreq1:
                print(f"{right} is not in s1")
                if len(countFreq2) > 0:
                    countFreq2.clear()
                left = right + 1
                print(f"countFreq2 cleared: {countFreq2}")
                continue
            countFreq2[s2[right]] +=1 #add to the freq map 
            if (right - left + 1) == len(s1):
                if countFreq2 == countFreq1:
                    return True
                else:
                    self.UpdateMap(countFreq2, s2[left])
                    left +=1
        return False
                 
