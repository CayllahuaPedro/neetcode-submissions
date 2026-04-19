class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTableS = {}
        hashTableT = {}
        for char in s:
            if char in hashTableS: 
                hashTableS[char] += 1
            else:
                hashTableS[char] = 1
        for char in t:
            if char in hashTableT: 
                hashTableT[char] += 1
            else:
                hashTableT[char] = 1
        
        return hashTableS == hashTableT
