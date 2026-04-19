class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ocurrencias = {}

        for number in nums:
            if number in ocurrencias:
               ocurrencias[number]+=1
            else:
                ocurrencias[number]= 1
        
        for number,freq in ocurrencias.items():
            if freq > 1: 
                return True
            else: 
                pass
                
        return False