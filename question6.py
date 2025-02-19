def encode_string(text: str) -> str:
  """
  Encode the input string using a custom encoding method.
  Args:
    text (str): The input string to encode
  Returns:
    str: The encoded string
  """

  return " ".join([str(ord(char)) for char in text])
  # TODO: Implement encoding logic


def decode_string(encoded_text: str) -> str:
  """
  Decode the encoded string back to original text.
  Args:
    encoded_text (str): The encoded string to decode
  Returns:
    str: The decoded original string
  """
  # TODO: Implement decoding logic

  return ''.join([chr(int(char)) for char in encoded_text.split(" ")])


# Test cases
if __name__ == "__main__":
  test_string = "Hello World!"
  
  # Test encoding
  encoded = encode_string(test_string)
  print(f"Original: {test_string}")
  print(f"Encoded: {encoded}")
  
  # Test decoding
  decoded = decode_string(encoded)
  print(f"Decoded: {decoded}")