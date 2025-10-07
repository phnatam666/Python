class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0      # Store the sign first
        x = abs(x)       # Then take absolute value

        rev = 0
        while x > 0 or x < 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        return -rev if neg else rev

x = (123)
sol = Solution()
result = sol.reverse(x)
print (result)
