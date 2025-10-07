from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def per(nums, start=0):
            n = len(nums)           

            if start == n:
                result.append(nums[:])
                return
            
            for i in range (start, n):
                nums[start], nums[i] = nums[i], nums[start]
                per(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]
        per(nums)
        return result
        

sol = Solution()
print(sol.permute([1, 2, 3]))
