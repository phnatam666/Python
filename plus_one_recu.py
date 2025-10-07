from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def helper(i):
            # Base case: if index < 0, means carry all the way, add 1 at front
            if i < 0:
                digits.insert(0, 1)
                return

            if digits[i] < 9:
                digits[i] += 1
            else:
                digits[i] = 0
                helper(i-1)

        helper(len(digits) - 1)
        return digits
    
s = Solution()
print(s.plusOne([1,2,3, 9]))  # Output: [1,2,4]