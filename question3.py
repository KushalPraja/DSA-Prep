def is_anagram(s: str, t: str) -> bool:
  if (s=="") and (t=="") : return True  
  if len(s)!=len(t): return False
  
  s=list(s)
  t=list(t)


  for i in range(len(s)):
    char=s[i]
    if char in t:
      t.pop(t.index(char)) 

  

  if t==[] :
    return True
  else:
    return False


  """
  Check if two strings are valid anagrams of each other.
  
  Args:
    s (str): First string
    t (str): Second string
    
  Returns:
    bool: True if strings are anagrams, False otherwise
  """


# Test cases
if __name__ == "__main__":
  print(is_anagram("anagram", "nagaram"))  # Should return True
  print(is_anagram("rat", "car"))          # Should return False
  print(is_anagram("", ""))                # Should return True
  print(is_anagram("a", "ab"))              # Should return False
  print(is_anagram("ab", "a"))              # Should return False
  print(is_anagram("aa", "a"))              # Should return False
  print(is_anagram("cinema", "iceman"))     # Should return True
  print(is_anagram("hello", "world"))       # Should return False