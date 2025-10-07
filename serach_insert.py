from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        else:
            inserted_value = target
            nums.append(inserted_value)
            nums.sort()
            return (nums.index(inserted_value))

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 7))  # Output: 2
