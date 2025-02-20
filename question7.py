def product_except_self(nums):
  """
  Given an array nums, return an array where each element at index i 
  is the product of all numbers in nums except nums[i]
  
  Args:
    nums (List[int]): Array of integers
  Returns:
    List[int]: Array where each element is product of all numbers except self
  """
  # TODO: Implement solution
  pass

  product={};

  # prefix product

  prefix_product=1
  for i in range(len(nums)):
    product[i]=prefix_product
    prefix_product*=nums[i]
  # suffix product

  suffix_product=1
  for i in range(len(nums)-1,-1,-1):
    product[i]*=suffix_product
    suffix_product*=nums[i]

  return [product[i] for i in range(len(nums))]
# 1,2,3,4 -> 24,12,8,6
  # key would be index, value would be 

# Test cases
if __name__ == "__main__":
  # Example test cases
  print(product_except_self([1, 2, 3, 4]))  # Should return [24, 12, 8, 6]
  print(product_except_self([-1, 1, 0, 3, -3]))  # Should return [0, 0, 9, 0, 0]