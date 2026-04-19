class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numeros= set(nums)
        maxLength = 0
        for i in range (0,n):
            currNum= nums[i]
            if currNum -1 in numeros:
                pass
            # aca podemos o deberiamos poder
            # afirmar que es un inicio de subseq
            tempLength =0
            while currNum in numeros: 
                tempLength+=1
                currNum += 1
            if tempLength > maxLength : 
                maxLength= tempLength
        return maxLength