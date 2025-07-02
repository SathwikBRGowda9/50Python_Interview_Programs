# 50. Missing Number in List
nums = list(map(int, input("Enter numbers 1 to N with one missing: ").split()))
n = len(nums) + 1
expected_sum = n * (n + 1) // 2
print("Missing number:", expected_sum - sum(nums))
