def contains_duplicate(nums):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
          return True
    return False

# Example usage
if __name__ == "__main__":
  test_array = [1, 2, 3, 1]
  result = contains_duplicate(test_array)
  print(f"Contains duplicate: {result}")  # Should print True
  
  test_array2 = [1, 2, 3, 4]
  result2 = contains_duplicate(test_array2)
  print(f"Contains duplicate: {result2}")  # Should print False