import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = math.log(n, 2)
        if n == 2**round(x):
            result = True
        else:
            result = False
        return result

n = 00
sol = Solution()
Result = sol.isPowerOfTwo(n)
print(Result)
            

        
         
