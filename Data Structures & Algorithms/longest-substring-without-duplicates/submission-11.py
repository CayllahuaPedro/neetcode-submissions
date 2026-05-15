class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupChar = {} # char : lastIndex
        left = 0
        maxLength =0 
        for i in range(len(s)):
            char = s[i]
            if char in dupChar:
                if dupChar[char] >= left:
                    left = dupChar[char] + 1
            dupChar[char] = i
            maxLength = max(maxLength, i - left + 1)
        return maxLength

