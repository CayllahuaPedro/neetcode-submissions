class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
          return ''
        left = 0
        need = 0
        have = 0
        countT = {}
        countW = {}
        res = [-1, -1]
        minLen = float('infinity')
        for char in t:
          if (countT.get(char, 0) == 0) : 
            need+=1 
          countT[char] = 1 + countT.get(char, 0)
        for right in range(len(s)):
          char = s[right]
          print("char", char)
          countW[char] = 1 + countW.get(char, 0)
          print("condition 1: " , char in countT and countW[char] == countT[char])
          if char in countT and countW[char] == countT[char]:
            have+=1 
          print("have", have)
          while have == need:
            print("min len condition",right - left + 1 < minLen)
            if (right - left + 1) < minLen:
              minLen = right - left +1 
              res = [left, right]
            countW[s[left]] = countW.get(s[left], 0) - 1
            if s[left] in countT and countT[s[left]] > countW[s[left]]:
              have-=1
            left +=1 
            print(f" have: {have}")
          
        l, r= res 
        return s[l: r+1] if minLen != float('infinity') else ''