from collections import defaultdict

def group_anagrams(strs):
  # group=[]
  # def check_anagram(str1,str2):
  #   return sorted(str1)==sorted(str2)
      
  # i=0
  # while (strs!=[]):
  #   # set first one 
  #   string1=strs.pop(0)
  #   inside_group=[string1];
  #   remaining=[]
  #   for i in range(len(strs)):
  #     if check_anagram(string1,strs[i]):
  #       inside_group.append(strs[i])
  #     else:
  #       remaining.append(strs[i])
  #   group.append(inside_group)
  #   strs=remaining
          
  # return group
  
  res = defaultdict(list)  # default value is list

  for s in strs:  # s is a string
    count= [0] * 26 # a .. z 
    
    for c in s: # c is a character in s
      count[ord(c)-ord("a")] += 1 # set a =0 and b to 1 example: "eat" -> [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    
    res[tuple(count)].append(s) # tuple(count) is a key, s is a value
    # in this case it is a hash map, key is a tuple of count, value is a list of strings

    # example map
  return res.values()
  
  """
  Given an array of strings strs, group the anagrams together.
  An anagram is a word formed by rearranging the letters of another word.
  
  Example:
  Input: strs = ["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
  
  Args:
    strs: List[str] - list of strings to group
  Returns:
    List[List[str]] - list of grouped anagrams
  """
  # TODO: Implement the grouping of anagrams
  # Hint: Consider how to identify if two strings are anagrams
  # Hint: Think about sorting characters
  pass

# Test cases
if __name__ == "__main__":
  test_case1 = ["eat","tea","tan","ate","nat","bat"]
  test_case2 = [""]
  test_case3 = ["a"]
  
  print(group_anagrams(test_case1))  # Should group the anagrams together
  print(group_anagrams(test_case2))  # Edge case with empty string
  print(group_anagrams(test_case3))  # Edge case with single character