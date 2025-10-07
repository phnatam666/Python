
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0  # No jumps needed to reach index 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

sol = Solution()
print(sol.jump([2,3,6]))


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        jump = 0
        far = 0

        for i in range(n-1):
            far = max(far, i + nums[i])

            if i == count:
                jump += 1
                count = far
        
        return jump



