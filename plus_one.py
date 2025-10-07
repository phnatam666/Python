def plusOne(digits):
    n = len(digits)
    for i in range(n-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Example usage:
print(plusOne([1,2,3,9]))  # Output: [1,2 

digits = [1,2,3,9]
num_str = ''.join(map(str, digits))
num_str = int(num_str) + 1


result = list(map(int, str(num_str))) # Output: "123"
print(result)