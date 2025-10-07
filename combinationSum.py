class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # can reuse same element
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return result

# Example usage
sol = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(candidates, target))

# 2 apporach - backtracking
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, start, curr):
            if curr == target:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if curr + candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(path, i, curr + candidates[i])
                    path.pop()

        ans = []
        backtrack([], 0,0)

        return ans