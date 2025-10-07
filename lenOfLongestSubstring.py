class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate (s):
            if char in index and index[char] >= left:
                left = index[char] + 1
                index[char] = right
                max_length = max(max_length, right - left +1)
        return max_length

input_string = "abcabcbb"
sol = Solution()
result = sol.lengthOfLongestSubstring(input_string)
print(result)