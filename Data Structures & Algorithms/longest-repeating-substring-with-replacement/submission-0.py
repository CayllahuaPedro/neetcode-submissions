from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLength=0
        freqMap =defaultdict(int)

        for i in range(len(s)):
            freqMap[s[i]] +=1
            while (i-l+1) - max(freqMap.values()) > k:
                freqMap[s[l]]-=1
                l+=1
            maxLength =max(maxLength, i-l +1)

            
        return maxLength
8

