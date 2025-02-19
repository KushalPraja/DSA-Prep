def two_sum(nums: list[int], target: int) -> list[int]:
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        return [i,j]
  return []

// done


  """
  Given an array of integers nums and an integer target,
  return indices of the two numbers in nums such that they add up to target.
  
  You may assume that each input would have exactly one solution,
  and you may not use the same element twice.
  
  Args:
    nums: List of integers
    target: Target sum
  Returns:
    List containing two indices whose corresponding values sum to target
  
  Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1]
  """
  # TODO: Implement the solution here
  pass

# Test cases
test_nums = [2, 7, 11, 15]
test_target = 9
result = two_sum(test_nums, test_target)
print(f"Input: nums = {test_nums}, target = {test_target}")
print(f"Output: {result}")