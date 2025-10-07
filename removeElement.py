class Solution:
    def removeElement(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1    

        return write_index
    
num = [3,2,2,1,2,3]
val = 2
sol =Solution() 
print(sol.removeElement(num))
      