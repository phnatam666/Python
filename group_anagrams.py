from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = defaultdict(list)

        for word in strs:
            key = ' '.join(sorted(word))
            anagram[key].append(word)

        result = list(anagram.values())
        
        return sorted(result)

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))