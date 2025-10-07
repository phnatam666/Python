def missing_nums(nums):
    n = len(nums)
    expected = n * (n+1)//2

    return expected - sum(nums)



nums = [3,4,-1,1]
print(missing_nums(nums))