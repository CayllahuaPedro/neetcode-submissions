class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len (sanitized)
        right= n-1
        left = 0
        while (left < right): 
            if (sanitized[left]!= sanitized[right]):
                return False
            left+=1
            right-=1
            
        return True
