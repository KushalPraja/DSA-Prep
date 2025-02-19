def two_sum(nums: list[int], target: int) -> list[int]:
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        return [i,j]
  return []

# Test cases
test_nums = [2, 7, 11, 15]
test_target = 9
result = two_sum(test_nums, test_target)
print(f"Input: nums = {test_nums}, target = {test_target}")
print(f"Output: {result}")
