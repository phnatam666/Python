def numbers(p=None):
    if p is None:
        p = n
    if p > 100:
        return
    print(p)
    numbers(p + 1)

n = 1
print(numbers())
