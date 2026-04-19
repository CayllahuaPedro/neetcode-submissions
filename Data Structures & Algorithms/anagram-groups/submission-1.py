from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list) # dists of dicts
        #this loop is O(n*m)
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char)- ord('a')] += 1
            key = tuple(freq)
            groups[key].append(string)

        return list(groups.values())
            
            