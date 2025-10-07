from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 2, len(nums) - 1
        prev_val = 0
        prev_idx = 0
        while i >= 0:
            if nums[i] < nums[i+1]:
                pivot = i
                while j > pivot:
                    if  nums[j] > nums[i]:
                        prev_val  = nums[j]
                        prev_idx = j
                    j -= 1
                nums[i], nums[prev_idx] = nums[prev_idx], nums[i]
                nums = self._reverse(nums, pivot)
                return
            else:
                i -= 1
        self._reverse(nums, -1)

    def _reverse(self, arr, i):
        left, right = i+1, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

nums = [1,2,3]
Solution().nextPermutation(nums)
print(nums)
