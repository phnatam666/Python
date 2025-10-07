n = "123"

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

sum_fact = 0
for digit in n:
    sum_fact += factorial(int(digit))

print(sum_fact)
 