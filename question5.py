class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    """
    Returns the k most frequent elements in nums.
    """
    table={} # empty table key: number , value: frequency
    for num in nums:
      if num in table:
        table[num]+=1 # if value is already in table, increment the frequency
      else:
        table[num]=1 # if value is not in table, set the frequency to 1
    sorted_table = sorted(table.items(), key=lambda x: x[1], reverse=True)

    # 1st step: (value:1, key:3), (value:2, key:2), (value:3, key:1)
    return [sorted_table[i][0] for i in range(k)] # return the first k elements


      

# Test
if __name__ == "__main__":
  solution = Solution()
  test_nums = [1,1,1,2,2,3]
  k = 2
  result = solution.topKFrequent(test_nums, k)
  print(f"Numbers: {test_nums}")
  print(f"Top {k} frequent elements: {result}")

  # expected output: [1, 2]

  test_nums2 = [1]
  k2 = 1
  result2 = solution.topKFrequent(test_nums2, k2)
  print(f"Numbers: {test_nums2}")
  print(f"Top {k2} frequent elements: {result2}")


  # expected output: [1]

  test_num3 = [1,4,6,4,3,1,3,5,6,8,4,2,4,7,9,4]
  k3 = 3
  result3 = solution.topKFrequent(test_num3, k3)
  print(f"Numbers: {test_num3}")
  print(f"Top {k3} frequent elements: {result3}")

  # expected output: [4, 1, 3]