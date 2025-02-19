def two_sum(nums: list[int], target: int) -> list[int]:
  
  prevMap = {}
  for i, num in enumerate(nums):
    prevMap[num]=i
    diff=target-num # 9-2=7
    if diff in prevMap and prevMap[diff]!=i:
      return [prevMap[diff],i]
  



  return []

# Test cases
test_nums = [2, 7, 11, 15]
test_target = 9
result = two_sum(test_nums, test_target)
print(f"Input: nums = {test_nums}, target = {test_target}")
print(f"Output: {result}")
