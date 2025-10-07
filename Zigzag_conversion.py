class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
           return s

        # Step 1: Prepare a grid (list of lists)
        zigzag = [[' ' for _ in range(len(s))] for _ in range(numRows)]
        
        row = 0
        col = 0
        going_down = True

        for c in s:
            zigzag[row][col] = c

            if going_down:
                if row == numRows - 1:
                    going_down = False
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                if row == 0:
                    going_down = True
                    row += 1
                else:
                    row -= 1
                    col += 1

        # Step 2: Print the zigzag pattern
        # Instead of this:
        for r in zigzag:
            print(''.join(r))
            result = ""
        for r in zigzag:
                result += ''.join(r).replace(' ', '')
                         
        return result
 

# Test


s = "PAYPALISHIRING"
numRows = 3
sol = Solution()
result = sol.convert(s, numRows)
print(result)

    