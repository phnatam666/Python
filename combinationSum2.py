from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            prev = -1  # To skip duplicates
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # Skip duplicate numbers at the same recursive level
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # i+1 because each number can only be used once
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res

sol = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(sol.combinationSum2(candidates, target))