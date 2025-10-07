class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write_index = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                

        
        return write_index

num = [3,2,2,1,2,3] 

sol =Solution()
print(sol.removeDuplicates(num))
